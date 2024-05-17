from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from core.api_handler import apiOperationsHandler


router = APIRouter()

# Templates directory
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

