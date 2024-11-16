from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth_routes import auth_router

app = FastAPI()
_ = load_dotenv()


app.include_router(tags=["Authetication"], prefix="/api/v1/auth", router=auth_router)