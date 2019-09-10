import os

# Third-party libraries
import pyrebase


firebase_config = {
  "apiKey": os.environ.get("apiKey"),
  "authDomain": os.environ.get("authDomain"),
  "databaseURL": os.environ.get("databaseURL"),
  "projectId": os.environ.get("projectId"),
  "storageBucket": os.environ.get("storageBucket"),
  "messagingSenderId": os.environ.get("messagingSenderId"),
  "appId": os.environ.get("appId")
}

firebase = pyrebase.initialize_app(firebase_config)

db = firebase.database()
