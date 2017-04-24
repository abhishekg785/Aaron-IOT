# simply handles the reply for hello by the user
import re
import random

PRIORITY = 1

# take necessary actions
def handle(text, audio):
    print 'Handling music module'
    audio.speak('playing some music')


# validate the module for the text from the source ( user, server, bot etc )
def isValid(text):
    return bool(re.search(r'\bmusic|melod|song|\b', text, re.IGNORECASE))