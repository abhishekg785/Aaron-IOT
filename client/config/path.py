# path.py : handles the paths being used in the app

import os

CLIENT_STRING = 'client'
QUERY_MODULES_STRING = 'query_modules'

# project main directory
APP_PATH = os.path.normpath(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir), os.pardir))

# client dir path
CLIENT_PATH = os.path.join(APP_PATH, CLIENT_STRING)

# query module path
QUERY_MODULES_PATH = os.path.join(CLIENT_PATH, QUERY_MODULES_STRING)
