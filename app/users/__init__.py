from flask import Blueprint
from flask_restful import Api
from . import views

users = Blueprint('users', __name__)
user_api = Api(users)
user_api.add_resource(views.CreateAccount, '/signup')
