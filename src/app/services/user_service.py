from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.schemas.user_schema import UserCreate, UserUpdate


class UserService(ABC):

    @abstractmethod
    async def create_user(self, db: AsyncSession, user: UserCreate):
        pass

    @abstractmethod
    async def get_user_by_id(self, db: AsyncSession, user_id: int):
        pass

    @abstractmethod
    async def get_all_users(self, db: AsyncSession):
        pass

    @abstractmethod
    async def update_user(self, db: AsyncSession, user_id: int, user: UserUpdate):
        pass

    @abstractmethod
    async def delete_user(self, db: AsyncSession, user_id: int):
        pass