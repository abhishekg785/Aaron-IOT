"""
    author : abhishek goswami
    abhishekg785@gmail.com

    audio.py module
    simply handles all the i/o operations related to the audio
    such as user audio input and output
"""

import pyaudio  # handles the record and play of the audio files
import audioop  # lib for handling math operations on the audio file

class AudioHandler():

    def __init__(self):
        print 'Cons of the AudioHandler Invoked'
        self.pyaudio = pyaudio.PyAudio()

    """ invokeListener : Is inoked at the time the user says something.
    I have to use a keyword to determine whether the user wants to convey
    a command or not or Simply to activate out system
    I will be using 'Hiro' keyword for the moment

    How to find whether user has said anything or not
    Or
    There is any disturbance by the user or not
    We can achieve this using a threshold value i.e :
    """
    def invokeListener(self, KEYWORD):
        pass





