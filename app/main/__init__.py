from flask import flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAchemy
from flask_login import LoginManger
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask.exit.scss import Scss

login_manager=LoginManger()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

bootstrap=Bootstrap()
db=SQLAchemy()
photos=UploadSet('photos',IMAGES)
mail=Mail()


def create_app(config_name):
    
    app=flask(__name__)

    #configuring sass
    Scss(app)

    #creating app config

    app.config.from_object(config_options[config_name])


    #init flask ext
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app()
    mail.init__app(app)

    #reg blueprint
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')


    #config uploadset
    configure_uploads(app,photos)


    return app
