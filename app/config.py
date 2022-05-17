import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class Config:
    API_URL = "http://quotes.stormconsultancy.co.uk/random.json"
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")


class ProdConfig(Config):
   DATABASE_URL= os.getenv("DATABASE_URL").replace('postgres://', 'postgresql://')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig
}
