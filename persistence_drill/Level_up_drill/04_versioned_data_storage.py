# 04_versioned_data_storage.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import SessionLocal
from models import UserEmailHistory

app = FastAPI()

@app.post("/users/{user_id}/email")
def update_email(user_id: int, new_email: str):
    db: Session = SessionLocal()
    db.query(UserEmailHistory).filter(
        UserEmailHistory.user_id == user_id,
        UserEmailHistory.is_active == True
    ).update({UserEmailHistory.is_active: False})
    latest = db.query(func.coalesce(func.max(UserEmailHistory.version), 0)).filter_by(user_id=user_id).scalar()
    history = UserEmailHistory(user_id=user_id, email=new_email, version=latest + 1, is_active=True)
    db.add(history)
    db.commit()
    return {"version": history.version, "email": history.email}
