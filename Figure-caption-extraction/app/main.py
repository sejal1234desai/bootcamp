# app/main.py

from fastapi import FastAPI, Depends, HTTPException, Security, File, UploadFile, BackgroundTasks, Query, status
from fastapi.security.api_key import APIKeyHeader
from fastapi.responses import JSONResponse, StreamingResponse, PlainTextResponse
from sqlalchemy.orm import Session
from app import models, database
from dotenv import load_dotenv
from sqlalchemy import text
import os
import io
import csv
import logging
from app.schemas import PaperDetail
from sqlalchemy import func
from app.schemas import EntityTypeStats


# Logging Setup
logger = logging.getLogger("batch_ingest")
handler = logging.FileHandler("ingestion.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

app = FastAPI(
    title="Figure Caption Extraction API",
    description="API for extracting and analyzing scientific figures and their captions",
    version="1.0.0",
    contact={
        "name": "Sejal Desai",
        "email": "sejaldesai2001@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Key dependency
async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    raise HTTPException(status_code=403, detail="Could not validate API KEY")

# Convert list of dicts to CSV buffer
def to_csv(data, fieldnames):
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
    buffer.seek(0)
    return buffer



@app.get("/health", tags=["monitoring"])
def health_check(db: Session = Depends(get_db)):
    try:
        # Simple DB check
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get-pmc-ids", dependencies=[Depends(get_api_key)])
async def get_pmc_ids(file: UploadFile = File(...)):
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        return JSONResponse(content={"error": "File too large. Max size is 5 MB."}, status_code=400)
    if not (file.filename.endswith(".txt") or file.filename.endswith(".csv")):
        return JSONResponse(content={"error": "Invalid file type. Only .txt and .csv allowed."}, status_code=400)
    file.file.seek(0)
    pmc_ids = parse_pmc_ids_from_file(file)
    return {"count": len(pmc_ids), "pmc_ids": pmc_ids}

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Shared PMC ID parser
def parse_pmc_ids_from_file(file: UploadFile):
    content = file.file.read().decode("utf-8")
    pmc_ids = []
    if file.filename.endswith(".csv"):
        reader = csv.DictReader(io.StringIO(content))
        for row in reader:
            if 'pmc_id' in row and row['pmc_id'].strip():
                pmc_ids.append(row['pmc_id'].strip())
    else:
        for line in content.splitlines():
            if line.strip():
                pmc_ids.append(line.strip())
    return pmc_ids




@app.post("/batch-ingest", dependencies=[Depends(get_api_key)], status_code=status.HTTP_202_ACCEPTED)
async def batch_ingest(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        return {"error": "File too large. Max size is 5 MB."}
    if not (file.filename.endswith(".txt") or file.filename.endswith(".csv")):
        return {"error": "Invalid file type. Only .txt and .csv allowed."}
    file.file.seek(0)
    pmc_ids = parse_pmc_ids_from_file(file)
    if not pmc_ids:
        return {"message": "No PMC IDs found in the uploaded file."}

    def ingest_all():
        from app.ingestion import ingest_pmc_id
        for pmc_id in pmc_ids:
            try:
                ingest_pmc_id(pmc_id)
                logger.info(f"Ingested PMC{pmc_id}")
            except Exception as e:
                logger.error(f"Failed to ingest PMC{pmc_id}: {e}")

    background_tasks.add_task(ingest_all)
    return {"message": f"Batch ingestion started for {len(pmc_ids)} PMC IDs."}


@app.get("/ingestion-logs", dependencies=[Depends(get_api_key)])
def get_ingestion_logs(lines: int = Query(50, ge=1, le=1000)):
    try:
        with open("ingestion.log", "r") as f:
            all_lines = f.readlines()
        return PlainTextResponse("".join(all_lines[-lines:]))
    except FileNotFoundError:
        return PlainTextResponse("Log file not found.")

@app.get("/papers", dependencies=[Depends(get_api_key)])

def get_papers(
    format: str = "json",
    keyword: str = Query(None),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(models.Paper)
    if keyword:
        pattern = f"%{keyword.lower()}%"
        query = query.filter((models.Paper.title.ilike(pattern)) | (models.Paper.abstract.ilike(pattern)))
    total = query.count()
    papers = query.offset(offset).limit(limit).all()
    data = [{"id": p.id, "pmid": p.pmid, "title": p.title, "abstract": p.abstract} for p in papers]

    if format == "csv":
        headers = {"X-Total-Count": str(total), "X-Limit": str(limit), "X-Offset": str(offset)}
        return StreamingResponse(to_csv(data, ["id", "pmid", "title", "abstract"]), media_type="text/csv", headers=headers)

    return {"total": total, "limit": limit, "offset": offset, "data": data}

@app.get("/papers/{pmid}", response_model=PaperDetail, dependencies=[Depends(get_api_key)])
def get_paper_by_pmid(pmid: str, db: Session = Depends(get_db)):
    paper = db.query(models.Paper).filter(models.Paper.pmid == pmid).first()
    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")
    return paper


@app.get("/figures", dependencies=[Depends(get_api_key)])
def get_figures(
        format: str = "json",
        paper_id: int = Query(None),
        pmid: str = Query(None),
        limit: int = Query(10, ge=1, le=100),
        offset: int = Query(0, ge=0),
        db: Session = Depends(get_db)
):
    query = db.query(models.Figure)

    if paper_id:
        query = query.filter(models.Figure.paper_id == paper_id)
    elif pmid:
        paper = db.query(models.Paper).filter(models.Paper.pmid == pmid).first()
        if not paper:
            raise HTTPException(status_code=404, detail="Paper not found")
        query = query.filter(models.Figure.paper_id == paper.id)
    else:
        raise HTTPException(status_code=400, detail="Must provide either paper_id or pmid")

    total = query.count()
    figures = query.offset(offset).limit(limit).all()
    data = [{
        "id": f.id,
        "paper_id": f.paper_id,
        "caption": f.caption,
        "figure_url": f.figure_url,
        "entities_count": len(f.entities)
    } for f in figures]

    if format == "csv":
        headers = {"X-Total-Count": str(total), "X-Limit": str(limit), "X-Offset": str(offset)}
        return StreamingResponse(
            to_csv(data, ["id", "paper_id", "caption", "figure_url", "entities_count"]),
            media_type="text/csv",
            headers=headers
        )

    return {"total": total, "limit": limit, "offset": offset, "data": data}

@app.get("/entities", dependencies=[Depends(get_api_key)])
def get_entities(
    format: str = "json",
    figure_id: int = Query(None),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(models.Entity)
    if figure_id:
        query = query.filter(models.Entity.figure_id == figure_id)
    total = query.count()
    entities = query.offset(offset).limit(limit).all()
    data = [{"id": e.id, "figure_id": e.figure_id, "entity_text": e.entity_text, "entity_type": e.entity_type} for e in entities]

    if format == "csv":
        headers = {"X-Total-Count": str(total), "X-Limit": str(limit), "X-Offset": str(offset)}
        return StreamingResponse(to_csv(data, ["id", "figure_id", "entity_text", "entity_type"]), media_type="text/csv", headers=headers)

    return {"total": total, "limit": limit, "offset": offset, "data": data}


@app.get("/entities/stats", response_model=list[EntityTypeStats], dependencies=[Depends(get_api_key)])
def get_entity_type_stats(db: Session = Depends(get_db)):
    results = db.query(models.Entity.entity_type, func.count(models.Entity.id)) \
                .group_by(models.Entity.entity_type).all()
    return [{"entity_type": et, "count": count} for et, count in results]


@app.get("/search-pmc", dependencies=[Depends(get_api_key)])
def search_pmc(
        keyword: str = Query(..., min_length=3),
        max_results: int = Query(10, ge=1, le=100),
        db: Session = Depends(get_db)
):
    from app.ingestion import search_pmc_ids

    try:
        pmc_ids = search_pmc_ids(keyword, max_results)
        return {"keyword": keyword, "pmc_ids": pmc_ids}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


