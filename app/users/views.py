from flask_restful import Resource, reqparse
from flask import make_response

from app.database import db


class CreateAccount(Resource):
    """Resource for creating an account"""

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', required=True)
        self.reqparse.add_argument('phone_number', required=True,)
        self.reqparse.add_argument(
            'device_tags', required=True, action='append')
        self.reqparse.add_argument(
            'alert_receivers', required=True, action='append')

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
        try:
            res = db.child('users').push(user)
            tags = self.tags(device_tags, res.get('name'))
            db.child('devices').set(tags)
            return make_response(
                {"message": "Your account has been created succesfully"}, 201)
        except Exception as error:
            return make_response({"message": "User already exists"}, 403)

    def get(self):
        response = db.child('users').get()
        return response.val()

    @staticmethod
    def tags(tags, key):
        return {tag: key for tag in tags}
