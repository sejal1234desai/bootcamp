from pydantic import BaseModel
from typing import List, Optional

class PostBase(BaseModel):
    title: str
    content: Optional[str] = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        orm_mode = True
