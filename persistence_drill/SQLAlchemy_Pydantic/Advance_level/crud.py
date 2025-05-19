from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from models import User, Post
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

async def get_user_with_posts(db: AsyncSession, user_id: int):
    try:
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            await db.refresh(user)
        return user
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error")

async def get_all_users_with_posts(db: AsyncSession):
    try:
        result = await db.execute(select(User).options(selectinload(User.posts)))
        return result.scalars().all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error")

async def insert_users(users_data: list, db: AsyncSession):
    try:
        for user_data in users_data:
            new_user = User(**user_data)
            db.add(new_user)
        await db.commit()  # Explicit commit is needed here
        return True
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

async def create_post(db: AsyncSession, post_data: dict, user_id: int):
    try:
        post = Post(**post_data, user_id=user_id)
        db.add(post)
        await db.commit()
        await db.refresh(post)
        return post
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")