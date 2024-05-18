from fastapi import APIRouter, Request, HTTPException, UploadFile, File,Query
from v1.serializers import *
from fastapi.templating import Jinja2Templates
from core.api_handler import apiOperationsHandler
from config import config


router = APIRouter()

# Templates directory
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/dashboard_page")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@router.get("/schedule_page")
async def schedule(request: Request):
    return templates.TemplateResponse("schedule.html", {"request": request})

@router.get("/course_page")
async def course(request: Request):
    return templates.TemplateResponse("course.html", {"request": request})

@router.get("/instructor_page")
async def instructor(request: Request):
    return templates.TemplateResponse("instructor.html", {"request": request})

@router.post("/login")
async def endpoint_to_login(
    data:LoginDetails
):
    print(data)
    if data.username == config.username and data.password == config.password:
        return {"details": "success"}
    else:
        raise HTTPException(status_code=403, detail=" Unauthorized access")
    
@router.post("/course")
async def endpoint_to_create_course(
    data:CourseCreate,
    # image: UploadFile = File(None)
):

    # Save image to server and get its path
    # if image:
    #     image_path = apiOperationsHandler.save_uploaded_image(image)
    # else:
    #     image_path = ""

    new_course = {
        "name":data.name,
        "level":data.level,
        "description":data.description,
        "image":""
    }
    response = apiOperationsHandler.save_course(new_course)
    if response:
        return {"details": response}
    else:
        raise HTTPException(status_code=404, detail="not found")

@router.get("/course")
async def endpoint_to_fetch_all_course(
):
    response = apiOperationsHandler.fetch_course()
    return {"details": response}

@router.post("/instructor")
async def endpoint_to_create_instructor(
    data:InstructorCreate,
):
    new_data = {
        "name":data.name,
        "contact":data.contact,
        "email":data.email,
        "address":data.address,
        "education":data.education
    }
    response = apiOperationsHandler.save_instructor(new_data)
    if response:
        return {"details": response}
    else:
        raise HTTPException(status_code=404, detail="not found")

@router.get("/instructor")
async def endpoint_to_fetch_all_instructor(
):
    response = apiOperationsHandler.fetch_instructor()
    return {"details": response}

@router.post("/schedule")
async def endpoint_to_create_schedule(
    data:ScheduleCreate,
):
    new_data = {
        "course": data.course,
        "instructor": data.instructor,
        "date": data.date
    }
    response = apiOperationsHandler.save_schedule(new_data)
    if response:
        return {"details": response}
    else:
        raise HTTPException(status_code=404, detail="not found")
    
@router.get("/schedule")
async def endpoint_to_fetch_all_schedule(
):
    response = apiOperationsHandler.fetch_schedule()
    return {"details": response}

@router.get("/schedule/course")
async def endpoint_to_fetch_all_valid_cources(
):
    response = apiOperationsHandler.fetch_valid_cources()
    return {"details": response}

@router.get("/schedule/instructor")
async def endpoint_to_fetch_all_valid_instructors(
    date: date = Query(..., description="The date to find instructors for")
):
    response = apiOperationsHandler.fetch_valid_instructors(date)
    return {"details": response}

# @router.get("/")
# async def root():
#     try:
#         if response:
#             response = apiOperationsHandler.fetchList()
#             return {"details": response}
#         else:
#             raise HTTPException(status_code=404, detail="Item not found")
#     except Exception as e:
#         raise HTTPException(status_code=400, detail="unsuccessful")

