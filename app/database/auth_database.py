from mysql import connector
from app.utils.exceptions_utils import AlreadyExistsException
from schemas.auth_schemas import UserCreate
from repositories.auth_repository import AuthRepository
from config.mysql_config import get_mysql_connection

class AuthDatabase(AuthRepository):
   async def create_user(self, user: UserCreate) -> UserCreate:
        try:
            conn = await get_mysql_connection()
            cursor = await conn.cursor()
            query = 'INSERT INTO USERS (NAME, LASTNAME, EMAIL, USERNAME, PASSWORD, PHOTO_PROFILE_URL) VALUES (%s, %s, %s, %s, %s, %s)'
            values = (user.name, user.lastname, user.email, user.username, user.password, user.photo_profile)
            await cursor.execute(query, values)
            await conn.commit()
            return user
        except connector.Error as e:
            if e.errno == 1062:
                raise AlreadyExistsException("User already exists")
            raise e
        finally:
            await cursor.close()
            await conn.close()
          
            
        
    