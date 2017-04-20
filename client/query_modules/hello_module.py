# simply handles the reply for hello by the user
import re
import random


# take necessary actions
def handle(text, audio):
    print 'Handling hello module'
    replies = ['hi!', 'yo!', 'hello!']
    message = random.choice(replies)
    audio.speak(message)


# validate the module for the text from the source ( user, server, bot etc )
def isValid(text):
    return bool(re.search(r'\bhi|hello|yo|hey there|hey\b', text, re.IGNORECASE))