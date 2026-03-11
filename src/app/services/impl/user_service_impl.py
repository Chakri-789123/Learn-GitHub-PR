from sqlalchemy.ext.asyncio import AsyncSession
from src.app.repositories.user_repo import UserRepository
from src.app.schemas.user_schema import UserCreate, UserUpdate
from src.app.services.user_service import UserService


class UserServiceImpl(UserService):

    def __init__(self):
        self.repo = UserRepository()

    async def create_user(self, db: AsyncSession, user: UserCreate):

        print("Starting user creation process")
        existing_user = await self.repo.get_user_by_email(db, user.email)

        if existing_user:
            raise ValueError("User already exists")
        new_user = await self.repo.create_user(db, user)
        print("User created successfully")

        return new_user

    async def get_user_by_id(self, db: AsyncSession, user_id: int):
        return await self.repo.get_user_by_id(db, user_id)

    async def get_all_users(self, db: AsyncSession):
        return await self.repo.get_all_users(db)

    async def update_user(self, db: AsyncSession, user_id: int, user: UserUpdate):
        return await self.repo.update_user(db, user_id, user)

    async def delete_user(self, db: AsyncSession, user_id: int):
        return await self.repo.delete_user(db, user_id)