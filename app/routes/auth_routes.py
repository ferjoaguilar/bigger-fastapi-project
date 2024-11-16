from fastapi import APIRouter, Body, HTTPException
from fastapi.responses import JSONResponse
from schemas.auth_schemas import UserCreate, SignupResponse
from database.auth_database import AuthDatabase
from services.auth_services import AuthServices
from utils import AlreadyExistsException


auth_router = APIRouter()
auth_repository = AuthDatabase()
auth_services = AuthServices(auth_repository)

@auth_router.post("/signup", 
                  description="Create a new manager", 
                  response_description="User created", 
                  response_model=SignupResponse, 
                  status_code=201
                )
async def signup(user:UserCreate = Body(...)):
    try:
        new_user = await auth_services.create_new_manager(user=user)
        return JSONResponse(status_code=201, content={"message": "User created", "data": {
            "name": new_user.name,
            "lastname": new_user.lastname,
            "email": new_user.email,
            "username": new_user.username,
            "photo_profile": new_user.photo_profile
        }})
    except AlreadyExistsException as e:
       raise HTTPException(status_code=e.status_code, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))