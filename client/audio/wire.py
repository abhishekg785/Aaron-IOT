"""
    author : abhishek goswami
    abhishekg785@gmail.com

    wire.py : make a wire b/w input and output  ( Record and play immediately )
"""

import pyaudio

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(
    format = p.get_format_from_width(WIDTH),
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
    )

print "--------------- Recording -----------------"
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    stream.write(data, CHUNK)

print "--------------- Done ---------------------"
stream.stop_stream()
stream.close()

p.terminate()