# creating the app package

from flask import Flask

app = Flask(__name__)

# imported at the bottom as the views.py needs the object app
from app import views