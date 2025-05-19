import argparse
import csv
import logging
from app.ingestion import ingest_pmc_id
from typing import Tuple
from app import database
from sqlalchemy.orm import Session

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




# Setup logging to file and console
logging.basicConfig(
    filename='batch_ingest.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def read_ids_from_txt(file_path):
    with open(file_path, "r") as f:
        ids = [line.strip() for line in f if line.strip()]
    return ids

def read_ids_from_csv(file_path, column_name='pmc_id'):
    ids = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(f"CSV Headers: {reader.fieldnames}")
        for row in reader:
            if column_name in row and row[column_name].strip():
                ids.append(row[column_name].strip())
    return ids


def process_pmc_id(pmc_id: str, db: Session) -> Tuple[bool, str]:
    """Process a single PMC ID with proper DB session handling"""
    try:
        result = ingest_pmc_id(pmc_id)
        if result is None:
            return False, f"PMC{pmc_id} was skipped (duplicate)"
        return True, f"PMC{pmc_id} ingested successfully"
    except Exception as e:
        logger.error(f"Error processing PMC{pmc_id}", exc_info=True)
        return False, f"PMC{pmc_id} failed: {str(e)}"
    finally:
        db.close()


def main() -> Tuple[int, int]:
    parser = argparse.ArgumentParser(description="Batch ingest PMC IDs from file")
    parser.add_argument("--file", required=True, help="Path to input file")
    parser.add_argument("--csv", action="store_true", help="Input is CSV format")
    parser.add_argument("--column", default="pmc_id", help="CSV column name for PMC IDs")
    args = parser.parse_args()

    # Read and deduplicate IDs

    try:
        pmc_ids = read_ids_from_csv(args.file, args.column) if args.csv else read_ids_from_txt(args.file)
    except Exception as e:
        logger.error(f"File reading failed: {str(e)}")
        return 0, 0

    unique_ids = list(dict.fromkeys(pmc_ids))  # Preserve order while deduping
    duplicate_count = len(pmc_ids) - len(unique_ids)

    if duplicate_count > 0:
        logger.warning(f"Removed {duplicate_count} duplicates from input file")

    logger.info(f"Processing {len(unique_ids)} unique PMC IDs")

    # Process with individual DB sessions per ID
    success_count = 0
    for i, pmc_id in enumerate(unique_ids, 1):
        db = database.SessionLocal()

        try:
            logger.info(f"[{i}/{len(unique_ids)}] Processing PMC{pmc_id}")
            success, message = process_pmc_id(pmc_id, db)
            if success:
                success_count += 1
            logger.info(message)
        except Exception as e:
            logger.error(f"Unexpected error processing PMC{pmc_id}: {str(e)}")
        finally:
            db.close()

    failure_count = len(unique_ids) - success_count
    logger.info(f"Batch complete. Success: {success_count}, Failures: {failure_count}")
    return success_count, failure_count


if __name__ == "__main__":
    main()