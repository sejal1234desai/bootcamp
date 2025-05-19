# 02_model_boundary_enforcement.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from pydantic import BaseModel
from database import get_db
from models import User

app = FastAPI()

class UserProfile(BaseModel):
    username: str
    email: str
    class Config:
        orm_mode = True

@app.put("/update-profile", response_model=UserProfile)
async def update_profile(user: UserProfile, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user.username))
    existing_user = result.scalar_one_or_none()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    existing_user.email = user.email
    await db.commit()
    return user
