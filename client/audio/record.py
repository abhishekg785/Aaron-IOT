"""
    author : abhishek goswami
    abhishekg785@gmail.com

    record.py : for recording the few seconds of audio and save it to wav file
"""
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORDS_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = CHUNK
    )

print "--------- Recording :) ---------------"
frames = []

for i in range(0, int(RATE / CHUNK * RECORDS_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print "------------ Done Recording :) ------------"
stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


