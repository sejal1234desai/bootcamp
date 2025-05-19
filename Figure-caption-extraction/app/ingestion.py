# app/ingestion.py
import requests
from app import models, database
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
import json
import traceback
from requests.exceptions import RequestException



def fetch_bioc_data(pmc_id: str):

    load_dotenv()
    ncbi_api_key = os.getenv("NCBI_API_KEY")

    url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC{pmc_id}/unicode"

    headers = {}
    if ncbi_api_key:
        headers["api-key"] = ncbi_api_key

    print(f"[INFO] Fetching: {url}")
    response = requests.get(url, headers=headers)

    print(f"[DEBUG] Status Code: {response.status_code}")
    print(f"[DEBUG] Content: {response.text[:300]}")  # show first 300 characters

    if response.status_code != 200:
        raise Exception(f"Failed to fetch BioC data: {response.status_code}")

    try:
        return response.json()
    except Exception as e:
        raise Exception(f"Invalid JSON: {e}")


def search_pmc_ids(keyword: str, max_results: int = 10):
    import os
    from dotenv import load_dotenv

    load_dotenv()
    ncbi_api_key = os.getenv("NCBI_API_KEY")

    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pmc",
        "term": keyword,
        "retmax": max_results,
        "retmode": "json"
    }

    if ncbi_api_key:
        params["api_key"] = ncbi_api_key

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to search PMC: {response.status_code}")

    try:
        data = response.json()
        pmc_ids = [id.replace("PMC", "") for id in data.get("esearchresult", {}).get("idlist", [])]
        return pmc_ids
    except Exception as e:
        raise Exception(f"Invalid JSON: {e}")


def extract_figures_and_metadata(bioc_json: list):
    # Initialize default return values
    title = ""
    abstract = ""
    figures = []

    # Safely navigate the BioC JSON structure
    try:
        if not bioc_json or not isinstance(bioc_json, list):
            return title, abstract, figures

        root = bioc_json[0]  # First item in list
        documents = root.get("documents", [])

        if not documents:
            return title, abstract, figures

        document = documents[0]  # Get first document
        passages = document.get("passages", [])

        for passage in passages:
            infons = passage.get("infons", {})
            section_type = infons.get("section_type", "")
            text = passage.get("text", "")

            if section_type == "TITLE":
                title = text
            elif section_type == "ABSTRACT":
                abstract += text
            elif section_type == "FIG":
                url = infons.get("figure_url", "").strip()
                if url and not url.startswith(("http://", "https://")):
                    url = None
                figures.append({
                    "caption": text,
                    "url": url
                })

    except Exception as e:
        print(f"[WARNING] Error parsing BioC data: {str(e)}")

    return title, abstract, figures




def ingest_pmc_id(pmc_id: str, max_retries: int = 3):
    db = next(database.get_db())

    try:
        # --- 1. Duplicate Check ---
        existing = db.query(models.Paper).filter(models.Paper.pmid == pmc_id).first()
        if db.query(models.Paper).filter(models.Paper.pmid == pmc_id).first():
            print(f"[SKIP] Duplicate PMC{pmc_id}")
            return None

        # --- 2. Fetch Data with Retries ---
        for attempt in range(max_retries):
            try:
                response = fetch_bioc_data(pmc_id)  # Your existing fetch function
                bioc_json = json.loads(response) if isinstance(response, str) else response
                break  # Success, exit retry loop
            except (json.JSONDecodeError, RequestException) as e:
                if attempt == max_retries - 1:
                    raise
                print(f"[RETRY {attempt + 1}/{max_retries}] PMC{pmc_id} JSON parse failed")
                continue

        # --- 3. Process Data ---
        title, abstract, figures = extract_figures_and_metadata(bioc_json)
        print(f"[PROCESSING] PMC{pmc_id} | {len(figures)} figures")

        # --- 4. Save with Transaction ---
        try:
            paper = save_to_database(pmc_id, title, abstract, figures, db)
            db.commit()
            print(f"[SUCCESS] Saved PMC{pmc_id} as Paper ID {paper.id}")
            return paper
        except Exception as e:
            db.rollback()
            print(f"[DB ERROR] Rollback PMC{pmc_id}: {str(e)}")
            raise

    except Exception as e:
        print(f"[FAILED] PMC{pmc_id} | Error: {str(e)}")
        print(traceback.format_exc())  # Detailed debug
        return None

    finally:
        db.close()



def fetch_entities(text: str):
    import re
    from typing import List, Dict
    patterns = {
        "GENE": r'\b[A-Z][A-Z0-9]+\b',
        "CHEMICAL": r'\b[A-Z][a-z]+\d*\b',
        "SPECIES": r'\b[A-Z][a-z]+ [a-z]+\b'
    }
    STOPWORDS = {"The", "Of", "And", "In", "On", "At", "For", "By", "With", "To", "From"}
    entities: List[Dict] = []
    for ent_type, pattern in patterns.items():
        matches = re.finditer(pattern, text)
        for match in matches:
            entities.append({
                "text": match.group(),
                "type": ent_type,
                "start": match.start(),
                "end": match.end()
            })

    return entities

def save_to_database(pmc_id: str, title: str, abstract: str, figures: list, db: Session):
        try:
            # Start a transaction
            paper = db.query(models.Paper).filter(models.Paper.pmid == pmc_id).first()

            if not paper:
                paper = models.Paper(pmid=pmc_id, title=title, abstract=abstract)
                db.add(paper)
                db.flush()  # Get the paper ID

            # Update paper details
            paper.title = title
            paper.abstract = abstract

            # Delete existing figures and entities in one operation
            db.query(models.Entity) \
                .filter(models.Entity.figure_id.in_(
                db.query(models.Figure.id) \
                    .filter(models.Figure.paper_id == paper.id)
            )).delete(synchronize_session=False)

            db.query(models.Figure) \
                .filter(models.Figure.paper_id == paper.id) \
                .delete(synchronize_session=False)

            # Add new figures and entities
            for fig in figures:
                if not fig.get("caption"):
                    continue

                figure = models.Figure(
                    caption=fig["caption"],
                    figure_url=fig.get("url"),
                    paper_id=paper.id
                )
                db.add(figure)
                db.flush()  # Get figure ID

                entities = fetch_entities(fig["caption"])
                for ent in entities:
                    db.add(models.Entity(
                        entity_text=ent["text"],
                        entity_type=ent["type"],
                        figure_id=figure.id
                    ))

            db.commit()
            return paper

        except Exception as e:
            db.rollback()
            raise Exception(f"Database save failed: {str(e)}")

