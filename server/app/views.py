"""
    author : abhishek goswami
    abhishekg785@gmail.com
    views.py : handling the routes
"""
from flask import render_template, request
from app import app

import sys

# watson api
import json
from watson_developer_cloud import ToneAnalyzerV3
from config import WATSON_API

#authenticate the application 
tone_analyzer = ToneAnalyzerV3(
    username = WATSON_API.TONE_ANALYZER_USERNAME,
    password = WATSON_API.TONE_ANALYZER_PASSWORD,
    version='2016-05-19 ')

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


# api using watson tone analyzer api
@app.route('/api/v0.1/watson/tone_analyzer', methods = ['GET', 'POST'])
def watson_tone_analyzer():
    if request. method == 'POST':
        query_text = request.form['text']
        print 'FETCHING DATA FOR THE TEXT'
        print query_text
        print '=========================================================='
        print(json.dumps(tone_analyzer.tone(text = query_text), indent=2))
    return render_template('watson_demo.html')


# api using watson natural language api
@app.route('/api/v0.1/watson/natural_language', methods = ['GET', 'POST'])
def watson_natural_language():
    print request.method
    return 'you are using watson natural language api'


@app.route('/demos/client')
def clientDemo():
    return render_template('clientDemo.html')
