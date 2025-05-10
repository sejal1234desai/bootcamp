:

📁 Real-Time File Processing System
A modular, fault-tolerant, and extensible file processing pipeline that supports single-file execution, continuous directory monitoring, and a live dashboard for tracking processing states.

🚀 Features
✅ Dual execution modes: Single file or watch mode

📊 Real-time Flask dashboard for monitoring

🔧 Configurable via CLI flags

🐳 Docker-compatible

🛠️ Makefile or run.sh supported

📂 Auto-handles folders: unprocessed/, underprocess/, and processed/

📦 Folder Structure
bash
Copy code
dataflow-framework/
│
├── abstraction-level-8/
│   ├── file_processor.py         # Core file processing logic
│   ├── watcher.py                # Watches folder for new files
│   ├── dashboard.py              # Flask web UI
│   ├── main.py                   # CLI entry point
│   ├── Makefile                  # Project automation
│   ├── run.sh                    # (Alternative) Shell-based runner
│   ├── requirements.txt
│   └── watch_dir/
│       ├── unprocessed/
│       ├── underprocess/
│       └── processed/
🛠️ Setup Instructions
🔧 Local Setup
Clone and navigate:

bash
Copy code
git clone https://github.com/sejal1234desai/bootcamp
cd dataflow-framework/abstraction-level-8
Set up virtual environment:

bash
Copy code
uv venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
🧪 Run Modes
🔹 Single File Mode
bash
Copy code
make input file=watch_dir/unprocessed/test.txt
This processes a single file and exits.

🔹 Watch Mode
bash
Copy code
make watch
This watches the watch_dir/unprocessed/ directory and processes any new files automatically.

🌐 Dashboard
While the app runs, open http://localhost:5000 to see:

Unprocessed files

Currently processing files

Completed files

Last processed file name

🐳 Docker Support
Build Image
bash
Copy code
docker build -t file-processor .
Run Container
bash
Copy code
docker run -p 5000:5000 file-processor --watch
📤 Uploading Files
Simply place files in the watch_dir/unprocessed/ folder.

(Optional) Implement FastAPI upload route or use rsync.

📡 Monitoring Uptime
You can use a free uptime service like Better Uptime to monitor your dashboard's availability.

🧼 Makefile Commands
Command	Description
make run	Default run with no arguments
make input	Process a single file
make watch	Watch mode for real-time processing
make clean	Clean processed directories (optional)
make docker	Build Docker image
