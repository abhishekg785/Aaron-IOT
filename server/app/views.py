"""
    author : abhishek goswami
    abhishekg785@gmail.com
    views.py : handling the routes
"""
from flask import render_template, request
from app import app

import sys
import os

# watson api
import json
from watson_developer_cloud import ToneAnalyzerV3
from config import WATSON_API

# adding client to the sys path to get the modules available here
CLIENT_PATH = os.path.normpath(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir), os.pardir))
sys.path.append(CLIENT_PATH + '/client/')

# getting the modules required for processing the query
from audio import AudioHandler
from processText import ProcessText
#getting watson functions
from watson import WatsonAPI

# Instantiate
audio = AudioHandler()
parser = ProcessText(audio)
watson_api = WatsonAPI()


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


# api using watson tone analyzer api
@app.route('/api/v0.1/watson/tone_analyzer', methods = ['GET', 'POST'])
def watson_tone_analyzer():
    if request. method == 'POST':
        query_text = request.form['text']
        print 'FETCHING DATA FOR THE TEXT'
        print query_text
        query_text = query_text.strip()
        print '=========================================================='
        watson_api.tone_analyzer_api(query_text)
    return render_template('watson_demo.html')


# api using watson natural language api
@app.route('/api/v0.1/watson/natural_language', methods = ['GET', 'POST'])
def watson_natural_language():
    if request.method == 'POST':
        query_text = request.form['text']
        query_text = query_text.strip()
        print query_text
    return render_template('watson_natural_demo.html')


@app.route('/demos/client')
def clientDemo():
    return render_template('clientDemo.html')
