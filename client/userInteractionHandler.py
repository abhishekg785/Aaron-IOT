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
            threshold, text = self.audioHandler.invokeListener('hello')
            if not text or not threshold:
            	print 'Nothing has been said'
            	continue
            print "keyword '%s' has been said!", text
            print "starting to listen for the user input command with threshold %f", threshold
            userInput = self.audioHandler.getUserAudioInput(threshold)
            if userInput:
                print userInput
            else:
                self.audioHandler.speak('Sorry, but i could not get it!');