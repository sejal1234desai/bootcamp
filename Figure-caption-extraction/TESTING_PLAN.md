══════════════════════════════════════════════════════════════════════
                              TESTING PLAN
          Figure Caption Extraction and Access System
══════════════════════════════════════════════════════════════════════

➤ PHASED APPROACH TO IMPLEMENTATION AND TESTING

I plan to divide the implementation and testing into three phases:

Phase 1: Basic ingestion and data extraction  
- Test fetching paper data from PubMed Central (PMC) and parsing figure captions.  
- Use a small set of known PMC IDs to verify data correctness.

Phase 2: API development and security  
- Build REST API endpoints for data submission and querying.  
- Test API key authentication to protect access.  
- Ensure correct JSON and CSV responses.

Phase 3: Batch processing and performance  
- Test ingestion with large lists of paper IDs through CLI and API.  
- Monitor response times and system behavior with increasing batch sizes.  
- Test error handling for invalid IDs or network issues.

──────────────────────────────────────────────────────────────────────
➤ FUNCTIONALITY TESTING

- Confirm that submitting a list of paper IDs triggers data ingestion correctly.  
- Verify that extracted figure captions, entities, and metadata match expected values.  
- Check the API endpoints to ensure they return data accurately in requested formats (JSON/CSV).  
- Test CLI commands for batch ingestion and configuration management.  
- Validate that admin configurations (like storage location, logging level) are respected.

──────────────────────────────────────────────────────────────────────
➤ SECURITY TESTING (API KEY)

- Ensure all API endpoints require a valid API key for access.  
- Test with invalid or missing API keys and verify that access is denied.  
- Verify that API keys are stored securely in environment variables or config files, not in source code.  
- Simulate unauthorized attempts and ensure system logs security-relevant events.

──────────────────────────────────────────────────────────────────────
➤ PERFORMANCE TESTING

- Measure response time for ingestion jobs with varying batch sizes (small: 5 IDs, medium: 50 IDs, large: 200+ IDs).  
- Monitor system resource usage (CPU, memory) during batch ingestion.  
- Ensure the API responds within acceptable time limits even under load.  
- Test graceful failure handling when API rate limits or external service errors occur.

──────────────────────────────────────────────────────────────────────
➤ MOCKED AND REAL DATA TESTING

- Use mocked API responses to test ingestion logic without relying on live external APIs.  
- Create sample PMC paper data with known figures and captions for consistent tests.  
- Run tests against real PMC paper IDs to validate end-to-end functionality.  
- Compare mocked test results with real data to ensure extraction accuracy.  
- Use automated test scripts (pytest or similar) for regression testing in future updates.

══════════════════════════════════════════════════════════════════════
