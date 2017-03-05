# This module controls the light related commands

import re


def handle(text, audio):
    """This function has to handle the turning on or off the lights
    If the lights are turned on , then turn off should occur and vise versa
    I have to fetch the action from the text and take the desired action
    """
    print 'handling light module'
    r = re.compile(r'\bon\b | \boff\b', flags=re.I | re.X)
    matchedWordArr = r.findall(text)
    arrLen = len(matchedWordArr)
    if arrLen == 1: # on or off
        action = matchedWordArr[0]
        print action
        audio.speak('I am turning' + action + ' the lights')
    elif arrLen == 0: # no action
        audio.speak('Please decide the action to perform with the lights!')
    elif arrLen >= 2: # ambigious
        audio.speak('Please decide the action first!')


def isValid(text):
    """check whether the word light or lights appear in the text
    or not and return the given bool val accordingly
    """
    return bool(re.search(r'\blight|lights\b', text, re.IGNORECASE))
