from fastapi import FastAPI
from routes.auth_routes import auth_router

app = FastAPI()


app.include_router(tags=["Authetication"], prefix="/api/v1/auth", router=auth_router)
