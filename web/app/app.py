import connexion
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(session_options={"autoflush": False})


def init_app():
    app = connexion.FlaskApp(
        __name__, port=80, specification_dir="/openapi/", options={"swagger_ui": True},
    )
    app.add_api("spec.yaml", arguments={"title": "Assignment task"})
    app.app.config.from_object("app.config.Config")

    db.init_app(app.app)
    Migrate(app.app, db)

    return app.app


application = init_app()
ma = Marshmallow(application)

