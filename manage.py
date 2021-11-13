from app import create_app, db
from app.models import Quotes
from flask_script import Manager, Server

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
  return dict(app=app, db=db, Quotes=Quotes)

if __name__ == '__main__':
    manager.run()