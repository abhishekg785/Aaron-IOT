"""
    author : abhishek goswami
    abhishekg785@gmail.com

    audio.py module
    simply handles all the i/o operations related to the audio
    such as user audio input and output
"""

import pyaudio  # handles the record and play of the audio files
import audioop  # lib for handling math operations on the audio file
import wave
import tempfile
import pyttsx

from stt import STTHandler


class AudioHandler:

    def __init__(self):
        print 'Cons of the AudioHandler Invoked'
        self._audio = pyaudio.PyAudio()
        self.STTHandler = STTHandler()

    def fetchThreshold(self):

        THRESHOLD_MULTIPLIER = 1.8
        RATE = 16000
        CHUNK = 1024

        # no of seconds to allow to establish threshold
        THRESHOLD_TIME = 1

        # recording system
        stream = self._audio.open(
            format = pyaudio.paInt16,
            channels = 1,
            rate = RATE,
            input = True,
            frames_per_buffer = CHUNK
        )

        # stores the audio data
        frames = []

        # stores the lastN score values
        lastN = [i for i in range(20)]

        # calculate the long ,run and average and thereby the proper threshold
        for i in range(0, RATE / CHUNK * THRESHOLD_TIME):

            data = stream.read(CHUNK)
            frames.append(data)

            # saves this data point as a source
            lastN.pop(0)
            lastN.append(self.getAudioRMS(data))
            average = sum(lastN) / len(lastN)

        print lastN
        stream.stop_stream()
        stream.close()

        # this will be set as a limit to cause the disturbance to be over
        THRESHOLD = average * THRESHOLD_MULTIPLIER

        return THRESHOLD

    def invokeListener(self, KEYWORD):
        """ Will be used to activate our system to listen for the commands
        when the user says something, in our case it will be a keyword.
        I will be using 'Hiro' keyword for the moment :P

        :param KEYWORD: The keyword through which the system will get a activated or starts listening for the commands
        """

        THRESHOLD_MULTIPLIER = 1.8  # will be used to check is user has said something or not

        # pyaudio parameters
        RATE = 16000
        CHUNK = 1024
        LISTEN_TIME = 10    # No of seconds to listen before forcing restart

        THRESHOLD_TIME = 1

        stream = self._audio.open(
            format = pyaudio.paInt16,
            channels = 1,
            rate = RATE,
            input = True,
            frames_per_buffer = CHUNK
        )

        # storing the audio data
        frames = []

        lastN = [i for i in range(30)]

        for i in range(0, RATE / CHUNK * THRESHOLD_TIME):
            print 'for the threshold time'
            data = stream.read(CHUNK)
            frames.append(data)

            lastN.pop(0)
            lastN.append(self.getAudioRMS(data))
            average = sum(lastN) / len(lastN)

        print lastN

        THRESHOLD = average * THRESHOLD_MULTIPLIER

        frames = []

        isDisturbance = False

        for i in range(0, RATE / CHUNK * LISTEN_TIME):
            print 'for the listen time'
            data = stream.read(CHUNK)
            frames.append(data)
            score = self.getAudioRMS(data)

            print 'score' + str(score)
            print 'thresh' + str(THRESHOLD)
            if score > THRESHOLD:
                isDisturbance = True
                print "Disturbance detected !"
                break

        if not isDisturbance:
            print "No Disturbance detected"
            stream.stop_stream()
            stream.close()
            return (None, None)

        frames = frames[-20:]

        DELAY_MULTIPLIER = 1
        for i in range(0, RATE / CHUNK * DELAY_MULTIPLIER):
            print 'for the the extra time'
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        # temporary file storage and finding the text in the audio file usig wit.ai cool!
        with tempfile.NamedTemporaryFile(mode='w+b') as f:
            wav_fp = wave.open(f, 'wb')
            wav_fp.setnchannels(1)
            wav_fp.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
            wav_fp.setframerate(RATE)
            wav_fp.writeframes(''.join(frames))
            wav_fp.close()
            f.seek(0)
            text = self.STTHandler.extractTextFromSpeech(f)
            print text

        text = str(text['_text'])
        text = text.split(' ')
        if any(KEYWORD in word for word in text):
            return (THRESHOLD, KEYWORD)

        return (False, text)

    def getAudioRMS(self, data):
        """Measure of the power in an audio signal
        :param data: chunk data of the audio file
        :return: calculated score
        """
        rms = audioop.rms(data, 2)
        score = rms / 3
        return score

    def getUserAudioInput(self, THRESHOLD = None, LISTEN = True):
        """Listens for the user audio input command
        Records until a seecond of silence or times out after 12 seconds
        Returns the first matching string or None
        :param THRESHOLD: The limit over which the disturbance occurs
        :param LISTEN: to listen or not
        :return: Speech converted to text using STTHandler module
        """
        text = self.getAllActiveInput(THRESHOLD, LISTEN)
        return text

    def getAllActiveInput(self, THRESHOLD = None, LISTEN = True):
        """Record the user audio input and times out after 12 seconds
        Returns a list of matching options or None
        :param THRESHOLD: The limit over which the disturbance occurs
        :param LISTEN: to listen or not
        :return: Speech converted to text using STTHandler module
        """

        RATE = 16000
        CHUNK = 1024
        LISTEN_TIME = 12

        # check if no threshold is provided
        if THRESHOLD is None:
            THRESHOLD = self.fetchThreshold();

        # play some audio here to indicate that our system has started listening bro :)
        self.speak('Give your command')

        # recodring stream
        stream = self._audio.open(
            format = pyaudio.paInt16,
            channels = 1,
            rate = RATE,
            input = True,
            frames_per_buffer = CHUNK
        )

        frames = []
        lastN = [THRESHOLD * 1.2 for i in range(30)]

        for i in range(0, RATE / CHUNK * LISTEN_TIME):

            print 'LISTENING FOR COMMANDS'
            data = stream.read(CHUNK)
            frames.append(data)
            score = self.getAudioRMS(data)

            lastN.pop(0)
            lastN.append(score)

            average = sum(lastN) / float(len(lastN))

            print 'average %f', average
            print 'threshold %f', THRESHOLD * 0.8
            if(average < THRESHOLD * 0.8):
                break

        print lastN
        # play another sound here to indicate that it has listened
        self.speak('Processing your request!')

        stream.stop_stream()
        stream.close()

        with tempfile.SpooledTemporaryFile(mode='w+b') as f:
            wav_fp = wave.open(f, 'wb')
            wav_fp.setnchannels(1)
            wav_fp.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
            wav_fp.setframerate(RATE)
            wav_fp.writeframes(''.join(frames))
            wav_fp.close()
            f.seek(0)
            text = self.STTHandler.extractTextFromSpeech(f)
            print text
            return text['_text']

    def speak(self, phrase):
        """converts the given text or phrase to the speech
        :param phrase: The text to be converted into speech
        """
        tts = pyttsx.init()
        tts.say(str(phrase))
        tts.runAndWait()






