from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.app.models.user_model import User
from src.app.schemas.user_schema import UserCreate, UserUpdate


class UserRepository:

    async def create_user(self, db: AsyncSession, user: UserCreate):
        new_user = User(
            name=user.name,
            email=user.email,
            password=user.password
        )

        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        return new_user


    async def get_user_by_id(self, db: AsyncSession, user_id: int):
        result = await db.execute(
            select(User).where(User.id == user_id)
        )

        return result.scalar_one_or_none()


    async def get_all_users(self, db: AsyncSession):
        result = await db.execute(
            select(User)
        )

        return result.scalars().all()


    async def update_user(self, db: AsyncSession, user_id: int, user: UserUpdate):

        db_user = await self.get_user_by_id(db, user_id)

        if not db_user:
            return None

        if user.name is not None:
            db_user.name = user.name

        if user.email is not None:
            db_user.email = user.email

        if user.is_active is not None:
            db_user.is_active = user.is_active

        await db.commit()
        await db.refresh(db_user)

        return db_user


    async def delete_user(self, db: AsyncSession, user_id: int):

        db_user = await self.get_user_by_id(db, user_id)

        if not db_user:
            return None

        await db.delete(db_user)
        await db.commit()

        return {"message": "User deleted successfully"}