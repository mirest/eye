from flask_restful import Resource, reqparse
from flask import make_response
from sqlalchemy import exc
from app.database import db
from app.users.models import User


class CreateAccount(Resource):
    """Resource for creating an account"""
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username')
        self.reqparse.add_argument('phone_number')
        self.reqparse.add_argument('device_tag')
        self.reqparse.add_argument('alert_receivers')

    def post(self):
        args = self.reqparse.parse_args()
        username = args['username']
        phone_number = args['phone_number']
        device_tag = args['device_tag']
        alert_receivers = args['alert_receivers']
        user = User(username=username,
                    phone_number=phone_number,
                    device_tag=device_tag,
                    alert_receivers=alert_receivers)
        try:
            db.session.add(user)
            db.session.commit()
            return make_response(
                {"message": "Your account has been created succesfully"}, 201)
        except exc.IntegrityError:
            db.session.rollback()
            check_user = user.query.filter_by(username=username).first()
            if check_user:
                return make_response({"message": "User already exists"}, 403)
