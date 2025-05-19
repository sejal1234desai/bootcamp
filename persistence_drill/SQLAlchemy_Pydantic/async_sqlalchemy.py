import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, ConfigDict


DATABASE_URL = "sqlite+aiosqlite:///./async_example.db"  # use asyncpg for PostgreSQL

Base = declarative_base()

class User(Base):
    __tablename__ = "async_users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

async def init_db():
    engine = create_async_engine(DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def add_user(name: str, email: str):
    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            session.add(User(name=name, email=email))
            print(f"Inserted user: {name}")

async def main():
    await init_db()
    await add_user("Async User", "async@example.com")

asyncio.run(main())
