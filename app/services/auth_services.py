from schemas.auth_schemas import UserCreate
from utils import hash_password
from repositories.auth_repository import AuthRepository


class AuthServices:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository
        
    async def create_new_manager(self, user: UserCreate):
        try:
            user.password = hash_password(password=user.password)
            return await self.auth_repository.create_user(user)
        except Exception as e:
            raise e