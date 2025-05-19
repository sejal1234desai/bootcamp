# 03_idempotent_upserts.py
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Product
from schemas import ProductCreate, ProductOut
from database import get_db

app = FastAPI()

@app.post("/upsert", response_model=ProductOut)
async def upsert_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.name == product.name))
    existing = result.scalar_one_or_none()
    if existing:
        existing.price = product.price
    else:
        existing = Product(name=product.name, price=product.price)
        db.add(existing)
    await db.commit()
    return existing
