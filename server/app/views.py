"""
    author : abhishek goswami
    abhishekg785@gmail.com
    views.py : handling the routes
"""
from flask import render_template, request
from app import app

import sys

# adding client to the sys path to get the modules available here
sys.path.append('/home/hiro/Documents/hiro/client/')

# getting the modules required for processing the query
from audio import AudioHandler
from processText import ProcessText

# Instantiate
audio = AudioHandler()
parser = ProcessText(audio)


@app.route('/')
@app.route('/index')
def index():
    return 'hello world'


# Route for handling the user query received through the url
@app.route('/parser/<text>')
def parseText(text):
    parser.parseText(text)
    return 'yo!'


# api for handling post request of the user query
@app.route('/api/v0.1/parse-query', methods = ['POST'])
def parseAPI():
    queryText = request.form['query']
    parser.parseText(queryText)
    return 'Yo!'

@app.route('/demos/sample')
def sample():
    return render_template('sample.html')