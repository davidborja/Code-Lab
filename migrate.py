import os

from app.integrations.db import db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app

flask_env = os.environ.get("FLASK_ENV")

if flask_env is None:
    flask_env = "local"

app = create_app(flask_env)

migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)

manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
    db.create_all()
