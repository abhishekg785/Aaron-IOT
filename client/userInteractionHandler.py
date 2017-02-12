"""
    author : abhishek goswami
    abhishekg785@gmail.com

    userInteractionHandler : handles the user interaction with the application
"""

from audio import AudioHandler

class UserInteractionHandler(object):

    def __init__(self):
        self.audioHandler = AudioHandler()

    def HandleUserInput(self):

        while True:
            obj = self.audioHandler.invokeListener('Hiro')
            if obj == True:
                break