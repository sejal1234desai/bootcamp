
📁 Real-Time File Processing System
A modular, fault-tolerant, and extensible file processing pipeline that supports both single-file execution and continuous directory watching. It includes a live Flask dashboard for real-time monitoring of file states.

🚀 Key Features
✅ Dual Execution Modes: Process a single file or continuously monitor a folder

📊 Live Flask Dashboard: Track files being processed in real-time

🔧 CLI Configurable: Run via CLI flags or Makefile

🐳 Docker Compatible: Containerized deployment supported

🛠️ Makefile & Shell Script Support: Easy automation with Makefile and run.sh

📂 Auto-organized Folders: Handles unprocessed/, underprocess/, and processed/ directories




📦 Project Structure
bash
Copy code
dataflow-framework/
└── abstraction-level-8/
    ├── file_processor.py     # Core file processing logic
    ├── watcher.py            # Monitors folder for new files
    ├── dashboard.py          # Flask dashboard for real-time tracking
    ├── main.py               # CLI entry point
    ├── Makefile              # Automation commands
    ├── run.sh                # Shell script alternative to Makefile
    ├── requirements.txt      # Python dependencies
    └── watch_dir/
        ├── unprocessed/      # Place files here to be processed
        ├── underprocess/     # Files currently being handled
        └── processed/        # Successfully processed files
🛠️ Setup Instructions
🔧 Local Setup
Clone the repository

bash
Copy code
git clone https://github.com/sejal1234desai/bootcamp
cd dataflow-framework/abstraction-level-8
Create and activate a virtual environment

bash
Copy code
uv venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
🧪 Execution Modes
🔹 Single File Mode
Process a single file and exit.

bash
Copy code
make input file=watch_dir/unprocessed/test.txt
🔹 Watch Mode
Continuously watch the unprocessed/ folder for new files and process them.

bash
Copy code
make watch
🌐 Dashboard Access
Once the application is running, open your browser and navigate to:

http://localhost:5000

Dashboard displays:

📥 Files in the queue (unprocessed)

🔄 Files currently being processed

✅ Files successfully processed

📁 Name of the last processed file

🐳 Docker Setup
🔹 Build Docker Image
bash
Copy code
docker build -t file-processor .
🔹 Run in Watch Mode with Dashboard
bash
Copy code
docker run -p 5000:5000 file-processor --watch
🔹 Run for Single File (example)
bash
Copy code
docker run -v "$(pwd)/watch_dir:/app/watch_dir" file-processor --input watch_dir/unprocessed/test.txt
📝 Ensure the watch_dir folder is mounted as a Docker volume for file accessibility.

📤 Uploading Files
To process files:

Drop them in the watch_dir/unprocessed/ folder (locally or inside Docker volume).

Optional enhancements:

Add a FastAPI upload route

Use tools like rsync or scp for automated upload from remote sources

📡 Monitoring Uptime
Use services like:

Better Uptime

UptimeRobot

to monitor availability of the dashboard at http://localhost:5000.

🧼 Makefile Commands
Command	Description
make run	Default run with no arguments
make input	Process a single file
make watch	Watch mode for real-time folder monitoring
make clean	Clean the processed directories
make docker	Build Docker image for deployment

✅ Project Achievements
You’ve implemented a functional file-processing system that includes:

🔧 Modular architecture

🔄 Real-time folder watcher

🌐 Live dashboard (Flask)

🖥️ CLI control via arguments or Makefile

🐳 Docker-compatible deployment

📈 Scalable and extensible design


📸 Dashboard Output
🧩Output -[ output_page.png]

🧩 Design Overview
Processing Logic: file_processor.py handles core operations.

CLI Interface: main.py controls single vs watch mode.

Watcher: watcher.py monitors file arrival.

Dashboard: dashboard.py shows live status on the web.

These components are decoupled to support modular upgrades and independent testing.

⚖️ Known Tradeoffs & Limitations
❌ No concurrent processing (one file at a time for simplicity)

❌ No database (in-memory state tracking only)

❌ Minimal error handling (logging/retries needed for production)

❌ No user authentication for dashboard

📈 Future Improvements
To scale this system or move to production:

🧵 Add multithreading/multiprocessing for concurrency

📦 Integrate Celery or Kafka for high-throughput tasks

🔐 Add authentication & file-type validation

📊 Connect Prometheus + Grafana for observability

🗃️ Use persistent database (e.g., PostgreSQL, Redis)

This architecture reflects the foundations of production frameworks like Apache Beam, Airflow, and Kafka Streams — but simplified for clarity and learning.

