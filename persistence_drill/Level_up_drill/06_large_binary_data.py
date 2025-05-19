# 06_large_binary_data.py
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from database import get_db
import os
import shutil

app = FastAPI()

@app.post("/upload/blob/{user_id}")
async def upload_blob(user_id: int, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    data = await file.read()
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404)
    user.profile_image_blob = data
    await db.commit()
    return {"message": "Stored as BLOB"}

@app.post("/upload/path/{user_id}")
async def upload_path(user_id: int, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404)
    os.makedirs("uploads", exist_ok=True)
    path = f"uploads/user_{user_id}.jpg"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    user.profile_image_path = path
    await db.commit()
    return {"message": "Stored as file path"}
