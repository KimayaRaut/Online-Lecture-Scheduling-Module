from mongoengine import Document,StringField
from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField
from mongoengine import signals
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Document):
    firstName = StringField(required=True)
    lastName = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    profilePicture = StringField()
    refreshToken = StringField()

    def payload(self):
        return{
            "firstName":self.firstName,
            "lastName":self.lastName,
            "email":self.email,
            "profilePicture":self.profilePicture,
        }
    
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        # print(document.password)
        document.password = pwd_context.hash(document.password)

    def isPasswordCorrect(self,plain_password):
        passwordFlag = pwd_context.verify(plain_password, self.password)
        # print("isPasswordCorrect",passwordFlag)
        return passwordFlag

    def generateAccessToken(self):
        return {}

    def generateRefreshToken(self):
        return {}  
    
signals.pre_save.connect(User.pre_save, sender=User)

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
    
 



