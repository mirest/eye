from flask_restful import Resource, reqparse
from flask import *

from app.database import db


class CreateAccount(Resource):
    """Resource for creating an account"""
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', required=True)
        self.reqparse.add_argument(
            'phone_number',
            required=True,
        )
        self.reqparse.add_argument('device_tags',
                                   required=True,
                                   action='append')
        self.reqparse.add_argument('alert_receivers',
                                   required=True,
                                   action='append')

    def post(self):
        args = self.reqparse.parse_args()
        username = args['username']
        phone_number = args['phone_number']
        device_tags = args['device_tags']
        alert_receivers = args['alert_receivers']

        user = {
            "username": username,
            "phone_number": phone_number,
            "alert_receivers": alert_receivers
        }
        return make_response(save_user(user, device_tags), 200)

    def get(self):
        response = db.child('users').get()
        return response.val()


def save_user(user, device_tags):
    try:
        res = db.child('users').push(user)
        set_tags(device_tags, res.get('name'))
        return {res.get('name'): user}
    except Exception as error:
        return {"message": "User already exists"}


def set_tags(tags, key):
    if isinstance(tags, list):
        [db.child('devices/' + tag).set({'owner': key}) for tag in tags]
    else:
        db.child('devices/' + tags).set({'owner': key})
