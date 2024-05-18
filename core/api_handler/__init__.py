from fastapi import UploadFile
import os
from v1.models import *

class APIOperations:
    def __init__(self) -> None:
        pass

    def save_uploaded_image(image: UploadFile, folder: str = "static/img") -> str:
        """
        Save the uploaded image to the specified folder on the server.
        Returns the path where the image is saved.
        """
        try:
            if not os.path.exists(folder):
                os.makedirs(folder)
            
            file_path = os.path.join(folder, image.filename)
            
            with open(file_path, "wb") as buffer:
                buffer.write(image.file.read())
            
            return file_path
        except Exception as e:
            print(e)
            return None
    
    def save_course(self,data: dict):
        try:
            print(data)
            course = Course(**data)
            course.save()
            return course
        except Exception as e:
            print(e)
            return None
    
    def fetch_course(self):
        try:
            courses = Course.objects().all()
            return [course.payload() for course in courses]
        except Exception as e:
            print(e)
            return None
    
    def save_instructor(self,data: dict):
        try:
            # print(data)
            instructor = Instructor(**data)
            instructor.save()
            return instructor
        except Exception as e:
            print(e)
            return None
        
    def fetch_instructor(self):
        try:
            instructor = Instructor.objects().all()
            return [instructor.payload() for instructor in instructor]
        except Exception as e:
            print(e)
            return None
    
    def save_schedule(self,data: dict):
        try:
            print(data)
            schedule = Schedule(**data)
            schedule.save()
            return schedule
        except Exception as e:
            print(e)
            return None
        
    def fetch_schedule(self):
        try:
            schedule = Schedule.objects().all()
            return [schedule.payload() for schedule in schedule]
        except Exception as e:
            print(e)
            return None
        
    def fetch_valid_cources(self):
        try:
            courses = Course.objects().all()
            return [course.fetch_valid_schedule_cource() for course in courses]
        except Exception as e:
            print(e)
            return None
        
    def fetch_valid_instructors(self,date):
        try:
            schedules = Schedule.objects(date=date).all()
            all_instructor = [schedules.fetch_instructor_name()["instructor_name"] for schedules in schedules]
            instructor = Instructor.objects().all()
            valid_list = []
            for instructor in instructor:
                if instructor.fetch_valid_schedule_instructor()["name"] in all_instructor:
                    pass
                else:
                    valid_list.append(instructor.fetch_valid_schedule_instructor())
            print(valid_list)
            return valid_list
        except Exception as e:
            print(e)
            return None

    # def fetchList(self):
    #     try:
    #         todo = TodoCollection.objects(name = "kimaya").first()
    #         print(todo)
    #         return todo.payload()
    #     except Exception as e:
    #         print(e)
    #         return None



apiOperationsHandler = APIOperations()