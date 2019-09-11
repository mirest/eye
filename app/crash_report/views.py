from flask_restful import Resource, reqparse
from flask import make_response, request, current_app
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
    messenger = MessageClient()
    user_to_in_danger = get_user(tag)
    body = f"ALERT !!!!\n{user_to_in_danger.get('username')} might be in danger\nContact them on phone number {user_to_in_danger.get('phone_number')}\nUser is at location {url}"  # noqa
    for number in user_to_in_danger.get('alert_receivers'):
        messenger.send_message(body, to=number)


def get_user(tag):
    uid = db.child('devices/'+tag).get().val()
    if uid:
        return db.child('users/'+uid).get().val()
    else:
        raise ValueError('not found')
