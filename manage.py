from app import create_app
from flask_script import Manage,Serve
from app import create_app,db
from app.models import User
from flask_migrate import Migrate,MigrateCommand

# Creating app instance
create_app('development')

manager=Manage(app)
manager.add_command('serve'Server)

#init the Migrate
migrate=Migrate(app,db)
manage.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db)

if __name__=='__main__':
    manager.run()