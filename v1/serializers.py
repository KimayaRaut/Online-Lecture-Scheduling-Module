from pydantic import BaseModel
from datetime import date

class userRegister(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str

class LoginDetails(BaseModel):
    username : str
    password: str

class CourseCreate(BaseModel):
    name: str
    level: str
    description: str

class InstructorCreate(BaseModel):
    name: str
    contact: str
    email: str
    address: str
    education: str

class ScheduleCreate(BaseModel):
    course: str
    instructor: str
    date: date