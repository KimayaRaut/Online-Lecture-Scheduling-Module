from fastapi import FastAPI
from v1.routes import router
from config import config
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import mongoengine


def create_app():
    app = FastAPI()

    app.include_router(router)

    # Mounting static files
    app.mount("/static", StaticFiles(directory="static"), name="static")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    DATABASE_HOST = config.DATABASE_HOST
    # print("DATABASE_HOST",DATABASE_HOST)
    mongoengine.connect(host=DATABASE_HOST)
    
    return app

app = create_app()