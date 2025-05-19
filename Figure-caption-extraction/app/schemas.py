# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class PaperBase(BaseModel):
    pmid: str
    title: str
    abstract: str



class PaperCreate(PaperBase):
    pass


class Paper(PaperBase):
    id: int

    created_at: Optional[datetime] = None  # Make optional
    updated_at: Optional[datetime] = None  # Make optional
    class Config:
        orm_mode = True


class FigureBase(BaseModel):
    caption: str
    figure_url: Optional[str]


class FigureCreate(FigureBase):
    paper_id: int


class Figure(FigureBase):
    id: int
    paper_id: int

    class Config:
        orm_mode = True


class EntityBase(BaseModel):
    entity_text: str
    entity_type: str


class EntityCreate(EntityBase):
    figure_id: int


class Entity(EntityBase):
    id: int
    figure_id: int

    class Config:
        orm_mode = True


class PaperDetail(Paper):
    figures: List[Figure] = []

    class Config:
        orm_mode = True


class EntityTypeStats(BaseModel):
    entity_type: str
    count: int