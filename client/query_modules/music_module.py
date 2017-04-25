# simply handles the reply for hello by the user
import re
import random

import os
import sys

import webbrowser

from random import randint

# getting the watson api functions here
PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(PATH)

MUSIC_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)) + '/music/'
# print MUSIC_PATH

from watson import WatsonAPI

watson = WatsonAPI()

# take necessary actions
def handle(text, audio):
    print 'Handling music module'
    """ fetch the text and get the emotion of the user
    go to the corresponding music dir and fetch the music
    play the music dud :)
    """
    tone = str(watson.tone_analyzer_api(text))
    music_list = os.listdir(MUSIC_PATH + tone + '/')
    music_list_len = len(music_list)
    if music_list_len > 0:
    	audio.speak('You seem to be ' + tone + '.I am playing a song for you!')
    	random_index = randint(0, music_list_len - 1)
    	print random_index
    	webbrowser.open(MUSIC_PATH + tone + '/' + music_list[random_index])
    else:
    	audio.speak('No music found')


# validate the module for the text from the source ( user, server, bot etc )
def isValid(text):
    return bool(re.search(r'\bmusic|melod|song|songs|tune\b', text, re.IGNORECASE))