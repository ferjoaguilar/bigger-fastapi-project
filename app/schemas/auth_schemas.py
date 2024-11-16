from pydantic import BaseModel, Field
from enum import Enum

class UserRoles(str, Enum):
    MANAGER = 'MANAGER'
    OWNER = 'OWNER'
    TOURIST = 'TOURIST'
    HOUSEKEEPER = 'HOUSEKEEPER'

""" class UserBase(BaseModel):
    userid: int = Field(...)
    name: str = Field(..., min_length=3, max_length=50)
    lastname: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., min_length=3, max_length=50)
    username: str = Field(..., min_length=3, max_length=25)
    password: str = Field(..., min_length=8, max_length=50)
    role: UserRoles = Field(...)
    photo_profile: str = Field(...)
    failed_login_attempts: int = Field(...)
    last_login_attempt: str = Field(...)
    locked: bool = Field(...)
    disabled: bool = Field(...) """

class UserBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    lastname: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., min_length=3, max_length=50)
    username: str = Field(..., min_length=3, max_length=25)
    password: str = Field(..., min_length=8, max_length=50)
    photo_profile: str | None = Field(None)

class UserCreate(UserBase):
    pass
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    "name": "Juan",
                    "lastname": "Perez",
                    "email": "juan1234@gmail.com",
                    "username": "juan1234",
                    "password": "juan1234",
                    "photo_profile": "https://www.imageurl.com/image.jpg",
                }
            ]
        }
    }


class SignupResponse(BaseModel):
    message: str = Field(...)
    data: UserCreate
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    "message": "User created",
                    "data": {
                        "name": "Juan",
                        "lastname": "Perez",
                        "email": "juan1234@gmail.com",
                        "username": "juan1234",
                        "photo_profile": "https://www.imageurl.com/image.jpg",
                    }
                }
            ]
        }
    }