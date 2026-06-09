import asyncio
from app.db.session import engine
from app.models.domain import Base

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Complete")

if __name__ == "__main__":
    asyncio.run(create_tables())