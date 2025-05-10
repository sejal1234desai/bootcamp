import argparse
import os
from file_processor import start_monitoring, process_single_file
from dashboard import app
import threading

# Function to run the Flask dashboard in a separate thread
def run_dashboard():
    app.run(debug=True, port=5000, use_reloader=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Processing System")
    parser.add_argument('--input', help="Process a single file", type=str)
    parser.add_argument('--watch', help="Watch mode to continuously process files", action='store_true')

    args = parser.parse_args()

    # Start the Flask dashboard in a separate thread
    dashboard_thread = threading.Thread(target=run_dashboard)
    dashboard_thread.daemon = True
    dashboard_thread.start()

    if args.watch:
        # Start watching for files in 'watch_dir/unprocessed'
        print("Starting watch mode...")
        start_monitoring()  # Start the monitoring function from file_processor.py
    elif args.input:
        # Process the single file provided
        print(f"Processing single file: {args.input}")
        process_single_file(args.input)  # New function to process a single file
