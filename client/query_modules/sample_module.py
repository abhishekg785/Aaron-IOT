# sample_module.py : a demo module
import re

# process more
def sample_module(text, audio):
    pass


# take necessary actions
def handle(text, audio):
    print 'Handling sample module'
    audio.speak('this is a sample module and it is working fine!')


# validate the module for the text from the source ( user, server, bot etc )
def isValid(text):
    """Return True if the given text is in context with the module
     or otherwise return False
    :param text: The input text to validate
    :return: Bool
    """
    return bool(re.search(r'\bsample\b', text, re.IGNORECASE))

