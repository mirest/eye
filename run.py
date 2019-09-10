import os

from app import create_app
from app.users.views import CreateAccount
from app.crash_report.views import CrushReport

from flask_restful import Api

config_name = "development"
app = create_app(config_name)
api = Api(app)

api.add_resource(CreateAccount, '/users')
api.add_resource(CrushReport, '/report')

if __name__ == "__main__":
    app.run()
