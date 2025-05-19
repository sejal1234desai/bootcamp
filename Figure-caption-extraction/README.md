──────────────────────────────────────────────────────────────────────         

                      FIGURE CAPTION EXTRACTION AND ACCESS SYSTEM
──────────────────────────────────────────────────────────────────────

Project Overview
─────

This project extracts figure captions, metadata, and biological entities from scientific research articles using PubMed Central APIs. The system is designed to be extensible, production-ready, and valuable for both researchers and developers.


Key Features
────

1. Extracts the following from PMC articles:
   - Title and abstract
   - Figure captions
   - Figure image URLs (if available)
   - Biological entities mentioned in figure captions (for example, genes)

2. Supports:
   - Ingestion via Command Line Interface (CLI) or REST API
   - Querying stored data through a secure REST API with API key authentication
   - Exporting results in JSON and CSV formats

3. Designed for:
   - Users interested in metadata from scientific papers
   - Administrators configuring storage and API access
   - Operations teams deploying and monitoring ingestion processes

──────────────────────────────────────────────────────────────────────   

USAGE
──

- To ingest papers:
  Use the CLI command or REST API endpoint to submit a list of paper IDs (PMC or PMID).

- To query data:
  Access the REST API with your API key to fetch paper details, figure captions, and associated entities in JSON or CSV formats.

- For administration:
  Configure storage location, logging level, API keys, and data sources via the configuration file or environment variables.

──────────────────────────────────────────────────────────────────────

TECHNOLOGY USED
────

- Python
- FastAPI (for REST API)
- SQLAlchemy (ORM)
- PostgreSQL (primary database)
- requests (for API calls to PMC and PubTator)
- python-dotenv (for configuration management)

──────────────────────────────────────────────────────────────────────
   
GETTING STARTED
─────

1. Clone the repository  
   git clone https://github.com/sejal1234desai/figure-caption-extraction  
   cd figure-caption-extraction

2. (Optional) Create and activate a virtual environment  
   uv venv venv  
   source venv/bin/activate   (Linux/macOS)  
   venv\Scripts\activate      (Windows)

3. Install dependencies  
   pip install -r requirements.txt

4. Set up the database (PostgreSQL recommended)  
   Create a PostgreSQL database and update your `.env` file with the connection credentials


──────────────────────────────────────────────────────────────────────

CONFIGURATION
─────

Create a `.env` file in the root directory with the following variables:

DB_URL=postgresql://sejal:sejal2001@localhost:5432/paperdb  
API_KEY=supersecretapikey

**Database Options**:  
- PostgreSQL (recommended for production):  
  `DB_URL=postgresql://user:password@localhost:5432/paperdb`  
- DuckDB (for lightweight local testing):  
  `DB_URL=duckdb:///local.db`



──────────────────────────────────────────────────────────────────────

 Demo (Terminal Walkthrough)

Experience the app through terminal-based demos recorded via asciinema:

🔹Asciinema Links
 - [Recording 1](https://asciinema.org/a/Zpo3bzfFZdqB7Jy73roy8Q4Zh)


- [Recording 2](https://asciinema.org/a/tPKzW7cD5tvabK1R0KzIMzZMo)

🔹 Ingesting PMC IDs

🔹 Fetching Papers and Figures

🔹 Entity Extraction Workflow

 ──────────────────────────────────────────────────────────────────────

DOCKER DEPLOYMENT
──────

Build the Docker image:

   docker build -t fig_api .

Run the container:

   docker run -d -p 8000:8000 --env-file .env_docker fig_api

The API will be accessible on localhost port 8000. Adjust `.env_docker` with your API key, database URL, and other settings.

 ──────────────────────────────────────────────────────────────────────
 
USAGE INSTRUCTIONS
────────

Ingest Data via CLI:  
   python app/ingest.py --input data/sample_ids.txt

Start REST API:  
   uvicorn app.api:app --reload

API Endpoints:  

GET /api/papers  
   Retrieve all papers

GET /api/papers/{id}  
   Retrieve a specific paper by ID

GET /api/figures/{paper_id}  
   Retrieve all figures for a paper

GET /api/entities/{figure_id}  
   Retrieve entities for a specific figure

API requests require the API key header:  
   X-API-Key: your_api_key_here

Example curl command:  
   curl -H "X-API-Key: your_api_key_here" http://localhost:8000/api/papers

Output Formats:  
- JSON via API  


Error Handling**:  
- Invalid PMC IDs: Logged and skipped (no job failure).  
- Rate Limits: Automatic retry with exponential backoff.  
- API Key Missing: HTTP 403 with JSON error: `{"detail": "API key required"}`.  

──────────────────────────────────────────────────────────────────────

PROJECT STRUCTURE
────────

figure-caption-api/  
  ├─ app/  
  │   ├─ clean_duplicates.py         (Duplicate data cleaning utilities)  
  │   ├─ ingest.py                   (CLI ingestion script)  
  │   ├─ models.py                   (SQLAlchemy models)  
  │   ├─ database.py                 (Database session and connection)  
  │   ├─ main.py                    (Application entry point)  
  │   └─ schemas.py                  (Pydantic schemas)  
  ├─ data/  
  │   └─ sample_ids.txt              (Example list of PMC IDs)  
  ├─ .env                           (Environment variables)  
  ├─ requirements.txt               (Python dependencies)  
  └─ README.md                     (Project documentation)  

──────────────────────────────────────────────────────────────────────

SAMPLE OUTPUT (JSON)
──────

{
  "paper_id": "123456",
  "title": "Understanding Genetic Pathways",
  "abstract": "This study investigates...",
  "figures": [
    {
      "caption": "Figure 1. Interaction between Gene X and Y.",
      "image_url": "https://example.com/image1.jpg",
      "entities": ["Gene X", "Gene Y"]
    }
  ]
}


OutPut Pages 



![First Page Output](imgs/first_page.png)

![Batch Ingestion Output](imgs/batch_ingestion.png)

![Figure Output](imgs/figure_output.png)

![Figures](imgs/figuress.png)



──────────────────────────────────────────────────────────────────────

DEMO AND PRESENTATION
───────

Screenshots and CLI/API demonstrations are included in the presentation HTML file.  
View the demo, presentation, and code at: 

https://sejal1234desai.github.io/My_page/



ABOUT THE DEVELOPER
─────

Created by Sejal Desai  
Portfolio: https://sejal1234desai.github.io/sejal-desaiportfolio-website/  
GitHub: https://github.com/sejal1234desai

 
