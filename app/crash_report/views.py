from flask_restful import Resource, reqparse
from flask import make_response, request, current_app
from sqlalchemy import exc
from datetime import datetime
from app.sms_utils import MessageClient

from app.database import db


class CrushReport(Resource):
    """Resource for creating an account"""

    def post(self):
        args = request.json
        now = datetime.now()
        args['created_at'] = now.strftime("%m-%d-%Y %H:%M:%S")
        res = db.child("reports").push(args)
        tag = args.get('device_tag')
        current_app.apscheduler.add_job(func=sendsms,
                                        trigger='date',
                                        args=[tag, args.get('location')], id='j'+str(res.get('name')))

        return make_response({"message": "Incident reported"}, 201)

    def get(self):
        response = db.child('reports').get()
        return response.val()


def sendsms(tag, location):
    url = f"https://www.google.com/maps?q={location.get('latitude')},{location.get('longitude')}"
    users = db.child('users').get().val()
    messenger = MessageClient()
    user_to_in_danger = [user
                         for user in users.values()
                         if user.get('device_tag') == tag]
    body = f"ALERT !!!!\n{user_to_in_danger[0].get('username')} might be danger\nContact them on phone number {user_to_in_danger[0].get('phone_number')}\nUser is at location {url}"  # noqa
    for number in user_to_in_danger[0].get('alert_receivers'):
        messenger.send_message(body, to=number)
