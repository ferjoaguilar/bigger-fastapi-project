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
        finally:
            await cursor.close()
            await conn.close()
          
            
        
    