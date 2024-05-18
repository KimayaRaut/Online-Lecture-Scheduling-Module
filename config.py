import os

class Config:
    def __init__(self, **args) -> None:
        self.username= args["username"]
        self.password = args['password']

        self.DATABASE_NAME = args["DATABASE_NAME"]
        self.DATABASE_HOST = args["DATABASE_HOST"]
        self.DATABASE_USERNAME = args["DATABASE_USERNAME"]
        self.DATABASE_PASSWORD = args["DATABASE_PASSWORD"]

        
config = Config(
    username="admin",
    password="admin",

    DATABASE_NAME="online_lecture_scheduling",
    DATABASE_HOST=os.getenv("DATABASE_HOST"),
    DATABASE_USERNAME="",
    DATABASE_PASSWORD="",
)