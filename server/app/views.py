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
# parser = ProcessText()


@app.route('/')
@app.route('/index')
def index():
    return 'This is the server for the Hiro project running on the port 8000! Yay!'



# Route for handling the user query received through the url
@app.route('/parser/<text>')
def parseText(text):
    parser.parseText(text)
    return 'yo!'


@app.route('/addMessage', methods = ['POST'])
def messageHandler():
    queryText = request.json['text']
    parser.parseText(queryText)
    return 'Yo!'


# api for handling post request of the user query
# /api/v0.1/parse-query
@app.route('/api/v0.1/parse-query', methods = ['POST'])
def parseAPI():
    queryText = request.json['query']
    parser.parseText(queryText)
    return 'Yo!'


@app.route('/demos/sample')
def sample():
    return render_template('sample.html')


@app.route('/demos/client')
def clientDemo():
    return render_template('clientDemo.html')