import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECURITY_PASSWORD_SALT = 'two_min_chance'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'ethicurean'
    SENDER_EMAIL = "toelapiut7@gmail.com"
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://toel:KingChase@localhost/ethicurean'

    DEBUG=True


config_options={
    'development':DevConfig,
    'production':ProdConfig
}