from app.app import db, application
from app import models

import flask_script
from flask_migrate import MigrateCommand


def _make_context():
    return dict(app=application, db=db, models=models)


def main():

    manager = flask_script.Manager(app)

    manager.add_command("runserver", flask_script.Server())
    manager.add_command("shell", flask_script.Shell(make_context=_make_context))
    manager.add_command("db", MigrateCommand)
