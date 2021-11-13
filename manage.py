from app import create_app, db
from app.models import Quotes, User, Comment
from flask_script import Manager, Server

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
  return dict(app=app, db=db, Quotes=Quotes, User=User, Comment=Comment)

if __name__ == '__main__':
    manager.run()