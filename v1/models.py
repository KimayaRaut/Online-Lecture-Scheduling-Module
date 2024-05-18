from mongoengine import Document,StringField

from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField


class Instructor(Document):
    name = StringField(required=True)
    contact = StringField()
    email = StringField()
    address = StringField()
    education = StringField()

    def payload(self):
        return{
            "name":self.name,
            "contact":self.contact,
            "email":self.email,
            "address":self.address,
            "education":self.education
        }
    
    def fetch_valid_schedule_instructor(self):
        return{
            "name":self.name,
        }


class Course(Document):
    name = StringField(required=True)
    level = StringField()
    description = StringField()
    image = StringField()
    # instructor = ListField(ReferenceField(Instructor))

    def payload(self):
        return{
            "name":self.name,
            "level":self.level,
            "description":self.description,
            "image":self.image,
            # "instructor":self.instructor
        }
    
    def fetch_valid_schedule_cource(self):
        return{
            "name":self.name,
        }


class Schedule(Document):
    course = StringField(required=True)
    instructor = StringField()
    date = DateTimeField()
    def payload(self):
        return{
            "course":self.course,
            "instructor":self.instructor,
            "date":self.date
        }
    
    def fetch_instructor_name(self):
        return{
            "instructor_name":self.instructor
        }