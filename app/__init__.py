from flask import Flask
from app.database import db

from app.config import app_config
from app.users import users


def create_app(config_name):
    app = Flask(__name__)
    conf = app.config.from_object(app_config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(users)
