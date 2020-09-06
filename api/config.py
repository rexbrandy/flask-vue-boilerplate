import os

class Config:
    DEBUG = True

    SECRET_KEY = 'hello_world'

    BASE_DIR = os.getcwd()

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False