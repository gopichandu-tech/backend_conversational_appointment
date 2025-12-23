from sqlalchemy.future import select
from app.models import User
from app.database import AsyncSessionLocal

async def user_exists(email: str) -> bool:
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none() is not None


async def save_user(data: dict):
    async with AsyncSessionLocal() as db:
        user = User(
            name=data["name"],
            email=data["email"],
            phone=data["phone"]
        )
        db.add(user)
        await db.commit()
