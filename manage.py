import os

from flask.ext.script import Manager, Server

from demo.app import create_app


app_root = os.path.dirname(os.path.abspath(__name__))

app = create_app('demo')
server = Server(port=os.environ['PORT'])
manager = Manager(app)
manager.add_command("runserver", server)


if __name__ == '__main__':
    manager.run()
