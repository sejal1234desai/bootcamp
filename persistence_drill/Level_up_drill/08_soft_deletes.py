# 08_soft_deletes.py
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal
from models import Product
from sqlalchemy import delete
from datetime import datetime, timedelta

async def cleanup_soft_deleted():
    async with AsyncSessionLocal() as session:
        threshold = datetime.utcnow() - timedelta(days=30)
        stmt = delete(Product).where(Product.deleted_at.isnot(None), Product.deleted_at < threshold)
        await session.execute(stmt)
        await session.commit()
        print("Old soft-deleted products purged.")

if __name__ == "__main__":
    asyncio.run(cleanup_soft_deleted())
