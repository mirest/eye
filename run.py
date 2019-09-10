import os

from app import create_app
from app.users.views import CreateAccount

from flask_restful import Api

config_name = "development"
app = create_app(config_name)
api = Api(app)

api.add_resource(CreateAccount, '/createaccount')

if __name__ == "__main__":
    app.run()
