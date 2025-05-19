# app/clean_duplicates.py
from sqlalchemy import func
from app.database import SessionLocal
from app import models


def remove_duplicate_papers():
    db = SessionLocal()

    # Find duplicate pmids
    duplicate_pmids = db.query(models.Paper.pmid) \
        .group_by(models.Paper.pmid) \
        .having(func.count(models.Paper.pmid) > 1) \
        .all()

    for (pmid,) in duplicate_pmids:
        # Get all papers with this pmid (ordered by id)
        papers = db.query(models.Paper) \
            .filter(models.Paper.pmid == pmid) \
            .order_by(models.Paper.id) \
            .all()

        # Keep the first one, delete others
        if len(papers) > 1:
            print(f"Found {len(papers)} duplicates for pmid {pmid}")
            for paper in papers[1:]:
                db.delete(paper)
            db.commit()

    db.close()


if __name__ == "__main__":
    remove_duplicate_papers()
    print("Duplicate cleanup complete")