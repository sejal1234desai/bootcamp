from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

class UserSchema(BaseModel):
    name: str
    email: str

# Create sqlite_basics DB
engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)
