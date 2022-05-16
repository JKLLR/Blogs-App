import os


class Config:
    """
    General parent configuration class
    """

    API_URL = "http://quotes.stormconsultancy.co.uk/random.json"

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://jeff:12345678@localhost/blogsapp"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST = "app/static/photos"

    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        Config: The parent configuration class with Generl configuration settings
    """

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    

class DevConfig(Config):
    """
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """

    DEBUG = True


config_options = {"development": DevConfig, "production": ProdConfig}