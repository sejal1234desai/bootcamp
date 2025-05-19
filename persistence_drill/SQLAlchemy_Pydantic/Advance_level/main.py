
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db, init_db
from crud import get_user_with_posts, insert_users, create_post, get_all_users_with_posts
from schemas import User, UserCreate, PostCreate, Post
from typing import List
import logging

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_with_posts(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/", response_model=List[User])
async def get_users(db: AsyncSession = Depends(get_db)):
    return await get_all_users_with_posts(db)

@app.post("/users/", response_model=dict)
async def create_users(users: List[UserCreate], db: AsyncSession = Depends(get_db)):
    try:
        users_data = [user.dict() for user in users]
        success = await insert_users(users_data, db)
        if success:
            return {"message": f"Successfully created {len(users)} users"}
    except HTTPException:
        raise
    except Exception as e:
        logging.exception("Error creating users")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/posts/", response_model=Post)
async def create_new_post(post: PostCreate, user_id: int, db: AsyncSession = Depends(get_db)):
    try:
        post_data = post.dict()
        return await create_post(db, post_data, user_id)
    except HTTPException:
        raise
    except Exception as e:
        logging.exception("Error creating post")
        raise HTTPException(status_code=500, detail="Internal server error")