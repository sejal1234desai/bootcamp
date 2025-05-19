
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import asynccontextmanager

# Database URL - update with your actual PostgreSQL credentials
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://newuser:newpassword@localhost/mydb"

# Create an async engine that connects to PostgreSQL database
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Session maker for creating DB sessions
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Declare a base class for ORM models
Base = declarative_base()

# Dependency to get the DB session
@asynccontextmanager
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db

# Function to initialize the database
async def init_db():
    # Create all tables defined in models
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
