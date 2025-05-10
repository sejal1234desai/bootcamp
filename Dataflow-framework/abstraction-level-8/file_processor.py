import shutil
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Directories for file states
UNPROCESSED_DIR = 'watch_dir/unprocessed'
UNDERPROCESS_DIR = 'watch_dir/underprocess'
PROCESSED_DIR = 'watch_dir/processed'


class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        """Triggered when a new file is created in the unprocessed directory."""
        if not event.is_directory and event.src_path.endswith('.txt'):
            print(f"New file detected: {event.src_path}")
            self.process_file(event.src_path)

    def process_file(self, file_path):
        """Process the file by simulating reading, moving it through stages."""
        try:
            filename = os.path.basename(file_path)
            # Move file to underprocess/
            dest_path = os.path.join(UNDERPROCESS_DIR, filename)
            shutil.move(file_path, dest_path)
            print(f"Processing file: {filename}")

            # Simulate processing by reading the file
            with open(dest_path, 'r') as file:
                print(f"Contents of {filename}: {file.read()}")

            # Move file to processed/
            processed_path = os.path.join(PROCESSED_DIR, filename)
            shutil.move(dest_path, processed_path)
            print(f"Finished processing file: {filename}")
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")


def process_single_file(file_path):
    """Process a single file as provided via CLI."""
    try:
        filename = os.path.basename(file_path)
        # Move file to underprocess/
        dest_path = os.path.join(UNDERPROCESS_DIR, filename)
        shutil.move(file_path, dest_path)
        print(f"Processing file: {filename}")

        # Simulate processing by reading the file
        with open(dest_path, 'r') as file:
            print(f"Contents of {filename}: {file.read()}")

        # Move file to processed/
        processed_path = os.path.join(PROCESSED_DIR, filename)
        shutil.move(dest_path, processed_path)
        print(f"Finished processing file: {filename}")
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")


def start_monitoring():
    """Start monitoring the unprocessed directory for new files."""
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, UNPROCESSED_DIR, recursive=False)
    observer.start()

    print(f"Watching directory {UNPROCESSED_DIR} for new files...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
