from abc import ABC, abstractmethod
from schemas.auth_schemas import UserCreate


class AuthRepository(ABC):
    @abstractmethod
    async def create_user(self, user: UserCreate) -> UserCreate:
        ...