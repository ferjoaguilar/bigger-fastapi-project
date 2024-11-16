from mysql import connector
from schemas.auth_schemas import UserCreate
from utils import AlreadyExistsException, hash_password
from repositories.auth_repository import AuthRepository


class AuthServices:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository
        
    async def create_new_manager(self, user: UserCreate):
        try:
            user.password = hash_password(user.password)
            return await self.auth_repository.create_user(user)
        except connector.Error as e:
            if e.errno == 1062:
                raise AlreadyExistsException("User already exists")
            raise e
        except Exception as e:
            raise e