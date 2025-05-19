
             DESIGN DOCUMENT
Figure Caption Extraction and Access System
Version: 1.0
Author: [Sejal Desai]



❖ PURPOSE
This document describes the proposed architecture, key components,
their interactions, dependencies, and deployment considerations
for a production-ready system that extracts figure captions and
related metadata from scientific publications.

──────────────────────────────────────────────────────────────────────
➤ SYSTEM ARCHITECTURE OVERVIEW
The system consists of four main layers:

  1. Data Ingestion Layer
     - Fetches paper metadata and figure captions from external APIs
       (e.g., PubMed Central, PubTator).
     - Processes raw data to extract figures, captions, and entities.
  
  2. Data Storage Layer
     - Stores structured data in a relational database (PostgreSQL).
     - Maintains tables for Papers, Figures, Entities with indexing for performance.

  3. API Layer
     - Provides REST endpoints for users to:
       • Submit paper ID lists for ingestion.
       • Query stored figure captions and entities.
     - Secured by API key authentication.

  4. Operational Layer
     - CLI tools for batch ingestion and configuration.
     - Docker container for consistent deployment.
     - Logging and monitoring for operational health.
  
  Extensibility**: New data sources (e.g., arXiv, Springer) can be added by:  
  1. Implementing a `DataSource` interface (e.g., `fetch_figures()`, `extract_entities()`).  
  2. Registering the module in the ingestion pipeline (no core changes required).  
  Example:  
  `-python
  class CustomDataSource(DataSource):  
      def fetch(self, paper_id):  
          # Custom logic for new API  
          return FigureData(...)  

──────────────────────────────────────────────────────────────────────
➤ KEY COMPONENTS AND INTERACTIONS

┌───────────────────┐          ┌───────────────────────┐
│ External APIs     │◀────────▶│ Data Ingestion Module  │
│ (PMC, PubTator)   │          │  - Fetches & processes │
└────────┬──────────┘          └─────────┬─────────────┘
         │                             │
         ▼                             ▼
┌───────────────────┐          ┌───────────────────────┐
│   PostgreSQL      │◀────────▶│    API Layer          │
│   Database        │          │  - Query & submission  │
│   (Tables: Papers,│          │  - API Key security    │
│    Figures,       │          └─────────┬─────────────┘
│    Entities)      │                    │
└───────────────────┘                    │
                                         ▼
                                ┌───────────────────┐
                                │ CLI & Operational │
                                │ Tools + Docker    │
                                └───────────────────┘

──────────────────────────────────────────────────────────────────────
➤ DEPENDENCIES AND JUSTIFICATIONS

➤ FastAPI
   - Chosen for modern, fast REST API development with async support.
   - Easy integration with security layers (API key).

➤ SQLAlchemy
   - Robust ORM for database interactions.
   - Supports PostgreSQL and other DBs for future flexibility.

➤ PostgreSQL
   - Reliable and scalable relational database.
   - Good indexing and JSON support for semi-structured data.

➤ Requests / HTTPX
   - For fetching data from external APIs reliably.

➤ Docker
   - Containerizes the application ensuring consistent environments.

➤ Python-dotenv
   - Manages environment configurations securely.
──────────────────────────────────────────────────────────────────────
➤ PostgreSQL
   - Chosen over DuckDB for production environments due to:  
     • Scalability for concurrent API and batch operations.  
     • Robust transactional support and indexing for complex queries.  
     • Compatibility with containerized deployments (e.g., Docker).  
   - DuckDB remains an option for local testing via configuration override.  

──────────────────────────────────────────────────────────────────────
➤ DEPLOYMENT CONSIDERATIONS

- The system will be containerized using Docker for portability.
- Configuration via environment variables (database URL, API key, logging level).
- The architecture supports adding new data sources by implementing
  new ingestion modules without changing the core API.
- Logs at different levels (info, debug) will aid debugging and monitoring.
- The ingestion jobs can be run interactively or in batch mode via CLI.

──────────────────────────────────────────────────────────────────────
➤ SIMPLE DEPLOYMENT DIAGRAM (ASCII)

  ┌───────────────┐           ┌───────────────┐
  │   User CLI /  │           │   User REST   │
  │  Batch Script │──────────▶│    API Calls  │
  └──────┬────────┘           └──────┬────────┘
         │                           │
         │                           │
  ┌──────▼────────┐          ┌───────▼────────┐
  │Ingestion Job  │          │    API Server   │
  │(Fetch & Parse│          │ (FastAPI + DB)  │
  └──────┬────────┘          └───────┬────────┘
         │                           │
         │                           │
   ┌─────▼────────────┐      ┌───────▼─────────┐
   │ PostgreSQL DB    │◀────▶│ SQLAlchemy ORM  │
   └──────────────────┘      └─────────────────┘

══════════════════════════════════════════════════════════════════════
