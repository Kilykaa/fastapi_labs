import asyncio
from app.db.session import SessionLocal
from app.models.domain import Store, Category, Product, User, UserProfile
from sqlalchemy.future import select

async def seed():
    async with SessionLocal() as session:
        result = await session.execute(select(Store))
        if result.scalars().first():
            return

        store1 = Store(name="Main Supermarket", address="Center Street 1")
        cat1 = Category(name="Groceries")
        cat2 = Category(name="Electronics")
        
        session.add_all([store1, cat1, cat2])
        await session.commit()
        await session.refresh(store1)
        await session.refresh(cat1)

        prod1 = Product(name="Bread", price=1.50, category_id=cat1.id, store_id=store1.id)
        prod2 = Product(name="Milk", price=2.00, category_id=cat1.id, store_id=store1.id)
        user1 = User(username="admin", email="admin@store.com", password="pwd", store_id=store1.id)
        
        session.add_all([prod1, prod2, user1])
        await session.commit()
        await session.refresh(user1)

        profile1 = UserProfile(user_id=user1.id, full_name="John Doe", shift_preference="Morning")
        session.add(profile1)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(seed())