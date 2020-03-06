import os

class Config():
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'b4d17b47db61ccb90f2cedfed7859bb4'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
