"""
    author : abhishek goswami
    abhishekg785@gmail.com

    program starts here :)
"""

from client import userInteractionHandler

class Hiro(object):

    def __init__(self):
        self.userInteraction = userInteractionHandler.UserInteractionHandler()

    def run(self):
        self.userInteraction.HandleUserInput()

if __name__ == '__main__':
    app = Hiro()
    app.run()