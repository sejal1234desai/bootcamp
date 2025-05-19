# 05_concurrency_handling.py
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models import Account

app = FastAPI()

@app.post("/transfer/naive")
async def naive_transfer(from_id: int, to_id: int, amount: float, db: AsyncSession = Depends(get_db)):
    from_acc = await db.get(Account, from_id)
    to_acc = await db.get(Account, to_id)
    if from_acc and to_acc and from_acc.balance >= amount:
        from_acc.balance -= amount
        to_acc.balance += amount
        db.add_all([from_acc, to_acc])
        await db.commit()
        return {"success": True}
    return {"success": False}

@app.post("/transfer/safe")
async def safe_transfer(from_id: int, to_id: int, amount: float, db: AsyncSession = Depends(get_db)):
    async with db.begin():
        result = await db.execute(select(Account).filter(Account.id.in_([from_id, to_id])))
        accounts = {a.id: a for a in result.scalars()}
        if len(accounts) < 2 or accounts[from_id].balance < amount:
            return {"success": False}
        accounts[from_id].balance -= amount
        accounts[to_id].balance += amount
        await db.commit()
    return {"success": True}
