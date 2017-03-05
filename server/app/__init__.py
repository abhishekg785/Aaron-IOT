# creating the app package

from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# imported at the bottom as the views.py needs the object app
from app import views