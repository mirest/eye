import os
from app.database import db
from app import create_app
from app.users.views import CreateAccount, save_user
from app.crash_report.views import CrushReport
from flask import *
from flask_restful import Api

config_name = "development"
app = create_app(config_name)
api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def isafe_account():
    if request.method == 'POST':
        if request.form['submit'] == 'Submit':
            user = {
                "username":
                request.form.get('uname'),
                "phone_number":
                request.form.get('number'),
                "alert_receivers": [
                    request.form.get('Alert Receiver1'),
                    request.form.get('Alert Receiver2')
                ]
            }
            device_tags = request.form.get('tag')
            user = save_user(user, device_tags)
            users = db.child('users').get().val()
        return render_template('users.html', users=users)
    return render_template('form.html')


api.add_resource(CreateAccount, '/users')
api.add_resource(CrushReport, '/report')

if __name__ == "__main__":
    app.run()
