from app import create_app
from flask_script import Manager,Server
from app import create_app,db
from app.models import User,Blog,Comment
from flask_migrate import Migrate,MigrateCommand
from datetime import datetime
# Creating app instance
app=create_app('development')

manager=Manager(app)
manager.add_command('server',Server)

#init the Migrate
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(
        username="toel12",
        email="toelapiut7@gmail.com",
        bio="I am a freelancer a model and a fashionist",
        password="admin",
        admin=True,
        confirmed_on=datetime.now())
    )
    db.session.commit()

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Blog=Blog,Comment=Comment)

if __name__=='__main__':
    manager.run()