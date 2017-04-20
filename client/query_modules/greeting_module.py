# A simple greeting handler for the user

import re


# take necessary actions
def handle(text, audio):
    print 'Handling Greeting module'
    audio.speak('I am fine! Thanks for asking')


# validate the module for the text from the source ( user, server, bot etc )
def isValid(text):
    """Return True if the given text is in context with the module
     or otherwise return False
    :param text: The input text to validate
    :return: Bool
    """
    return bool(re.search(r'\bhow are you|wassup\b', text, re.IGNORECASE))
