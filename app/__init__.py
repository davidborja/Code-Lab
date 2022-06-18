from app.integrations.ma import ma
from app.integrations.db import db

# flask
from flask import Blueprint
from flask_restx import Api
from flask import Flask
from flask_seeder import FlaskSeeder

from .config.config import config

# Documentation Swagger
from app.api.doc.shopping_statistics import shopping_statistics_ns

# Resources
from app.api.resources.shopping_statistics import ShoppingStatistics


def create_app(setting_module="local"):
    app = Flask(__name__, instance_relative_config=True)
    seeder = FlaskSeeder()

    app.config.from_object(config[setting_module])

    db.init_app(app)
    seeder.init_app(app, db)
    ma.init_app(app)

    blue_print = Blueprint("api", __name__, url_prefix="/api")
    api = Api(blue_print, doc="/doc", title="Shopping Center")

    app.register_blueprint(blue_print)

    api.add_namespace(shopping_statistics_ns)
    shopping_statistics_ns.add_resource(ShoppingStatistics, "")

    return app
