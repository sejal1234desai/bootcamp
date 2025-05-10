FINAL.md – Real-Time File Processing System
✏️ 1. Design Decisions
The primary architectural decision was to create a modular and extensible file processing system that supports both single-file execution and continuous directory watching. The system is designed around a clean separation of concerns:

Processing Logic (file_processor.py): Handles the business logic of reading and processing files.

CLI Interface (main.py): Controls how the application is run (via --input or --watch).

Dashboard (dashboard.py): Provides a Flask web dashboard showing file states in real-time.

Watcher (watcher.py): Monitors directories and initiates file processing.

The most useful abstraction was the decoupling between the watcher, processor, and dashboard. This separation allowed testing and enhancement of each component independently while ensuring they work together in the final pipeline.

⚖️ 2. Tradeoffs
Some simplifications were made to keep the project within scope:

Concurrency was omitted in favor of simplicity; files are processed one at a time to reduce risk of data races or corruption.

Security features such as file type validation or authentication for dashboard access were skipped for now.

Error handling was basic; in production, better logging and retry mechanisms would be necessary.

Current Limitations
No database persistence (all state is in-memory).

Not yet designed for high-throughput or distributed deployments.

Flask development server is used (not production-ready).

📈 3. Scalability
If the input volume increased 100x:

Parallel processing using multithreading or multiprocessing could be introduced in the watcher or processor.

A job queue like Celery or a streaming system like Apache Kafka could be used to scale file intake and processing.

Database storage could replace in-memory tracking for scalability and persistence.

🔐 4. Extensibility & Security
To prepare this system for real-world use:

Add user authentication and role-based access for the dashboard.

Use HTTPS and token-based authentication if exposing APIs for upload/download.

Implement file validation to prevent malicious uploads.

Add logging and monitoring tools like Prometheus and Grafana for observability.

✅ Achievements
You’ve successfully built a fully functional system that includes:

✅ Modular processing engine

✅ Stream-based folder monitor

✅ Web dashboard for file tracking

✅ CLI control for input and watch modes

✅ Docker and Makefile support for deployment

✅ Scalable and extensible architecture

This project mirrors core components found in production-grade systems like Apache Beam, Airflow, and Kafka-based processors.