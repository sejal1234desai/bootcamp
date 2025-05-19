# 09_large_dataset_testing.py
import asyncio
import time
import psutil
from models import Product
from database import AsyncSessionLocal

NUM_RECORDS = 1_000_000

def generate_product(i):
    return Product(name=f"Product {i}", price=10.0 + (i % 100))

async def insert_batch(batch_size=1000):
    print("Inserting products...")
    process = psutil.Process()
    start_time = time.perf_counter()
    start_mem = process.memory_info().rss

    async with AsyncSessionLocal() as session:
        for i in range(0, NUM_RECORDS, batch_size):
            batch = [generate_product(j) for j in range(i, min(i + batch_size, NUM_RECORDS))]
            session.add_all(batch)
            await session.flush()
        await session.commit()

    end_time = time.perf_counter()
    end_mem = process.memory_info().rss
    print(f"Inserted in {end_time - start_time:.2f}s, Memory used: {(end_mem - start_mem)/1024/1024:.2f}MB")

if __name__ == "__main__":
    asyncio.run(insert_batch())
