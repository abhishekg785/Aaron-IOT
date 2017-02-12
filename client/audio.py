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

class AudioHandler():

    def __init__(self):
        print 'Cons of the AudioHandler Invoked'
        self._audio = pyaudio.PyAudio()
        self.wave_output_file_name = 'output.wav'

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

        # record the audio file
        wf = wave.open(self.wave_output_file_name, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self._audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        return True


    def getAudioRMS(self, data):
        """Measure of the power in an audio signal
        :param data: chunk data of the audio file
        :return: calculated score
        """
        rms = audioop.rms(data, 2)
        score = rms / 3
        return score






