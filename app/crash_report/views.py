from flask_restful import Resource, reqparse
from flask import make_response, request
from sqlalchemy import exc
from datetime import datetime

from app.database import db


class CrushReport(Resource):
    """Resource for creating an account"""

    def post(self):
        args = request.json
        args['created_at'] = datetime.now().strftime("Y%.M%.D/HH:MM")
        res = db.child("reports").push(args)
        return make_response({"message": "Incident reported"}, 201)

    def get(self):
        response = db.child('reports').get()
        return response.val()
