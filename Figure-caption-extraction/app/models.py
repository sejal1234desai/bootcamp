# app/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey,Index,DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import DateTime
from datetime import datetime


class Paper(Base):
    __tablename__ = "papers"
    __table_args__ = (
        Index('idx_pmid_unique', 'pmid', unique=True),
    )

    id = Column(Integer, primary_key=True, index=True)
    pmid = Column(String, unique=True, index=True, nullable=False)
    title = Column(Text)
    abstract = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    figures = relationship("Figure", back_populates="paper")




class Figure(Base):
    __tablename__ = "figures"
    __table_args__ = (
        Index('ix_figure_paper_id', 'paper_id'),
    )


    id = Column(Integer, primary_key=True, index=True)
    paper_id = Column(Integer, ForeignKey("papers.id"))
    caption = Column(Text)
    figure_url = Column(Text)

    paper = relationship("Paper", back_populates="figures")
    entities = relationship("Entity", back_populates="figure")

class Entity(Base):
    __tablename__ = "entities"
    __table_args__ = (
        Index('ix_entity_figure_id', 'figure_id'),
        Index('ix_entity_type', 'entity_type'),
    )
    id = Column(Integer, primary_key=True, index=True)
    figure_id = Column(Integer, ForeignKey("figures.id"))
    entity_text = Column(Text)
    entity_type = Column(String)

    figure = relationship("Figure", back_populates="entities")
