from flask import Flask

from app.config import app_config
from app.users import users
from apscheduler.schedulers.background import BackgroundScheduler


def registerschedule(app):
    scheduler = BackgroundScheduler()
    app.apscheduler = scheduler
    scheduler.start()


def create_app(config_name):
    app = Flask(__name__)
    conf = app.config.from_object(app_config)
    app.config.from_pyfile('config.py')
    register_blueprints(app)
    registerschedule(app)
    return app


def register_blueprints(app):
    app.register_blueprint(users)


#  {% comment %} url_for('static', filename='iot.css', v=0.01) {% endcomment %}
