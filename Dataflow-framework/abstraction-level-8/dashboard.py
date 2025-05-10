from flask import Flask, render_template
import os

app = Flask(__name__)

WATCH_DIR = './watch_dir'
UNPROCESSED_DIR = os.path.join(WATCH_DIR, 'unprocessed')
UNDERPROCESS_DIR = os.path.join(WATCH_DIR, 'underprocess')
PROCESSED_DIR = os.path.join(WATCH_DIR, 'processed')


@app.route('/')
def index():
    unprocessed_files = os.listdir(UNPROCESSED_DIR)
    underprocess_files = os.listdir(UNDERPROCESS_DIR)
    processed_files = os.listdir(PROCESSED_DIR)

    # For the sake of simplicity, let's assume the last processed file is the last in the processed list
    last_processed = processed_files[-1] if processed_files else "No files processed yet"

    return render_template('index.html', unprocessed=unprocessed_files,
                           underprocess=underprocess_files, processed=processed_files,
                           last_processed=last_processed)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
