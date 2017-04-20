"""
	abhishekg785@gmail.com
	abhishek goswami

	stt.py : speech to text handler
"""
# i will be using wit.ai api for the speech to text conversion

from wit import Wit
from config import config


class STTHandler:
    def __init__(self):
        print "In the sttHandler class cons"
        self.client = Wit(access_token=config.ACCESS_TOKEN)

    def extractTextFromSpeech(self, f):
        resp = self.client.speech(f, None, {'Content-Type': 'audio/wav'})
        return resp
