from fastapi import FastAPI
from v1.routes import router
from config import config
from fastapi.staticfiles import StaticFiles
import mongoengine

def create_app():
    app = FastAPI()

    app.include_router(router)

    # Mounting static files
    app.mount("/static", StaticFiles(directory="static"), name="static")

    mongoengine.connect(db=config.DATABASE_NAME)
    
    return app

app = create_app()