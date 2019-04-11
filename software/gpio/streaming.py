import pyaudio
import numpy as np
import time
from pysndfx import AudioEffectChain

fx = (
	AudioEffectsChain()
	.highshelf()
	.reverb()
	.phaser()
	.delay()
	.lowshelf()
)

p=pyaudio.PyAudio()

CHANNELS = 1
RATE = 44100

def callback(in_data, frame_count, time_info, flag):
    return in_data, pyaudio.paContinue

stream = p.open(format=pyaudio.paInt16, 
		channels=CHANNELS, rate=RATE, output=True, input=True,
		stream_callback=callback)

stream.start_stream()

fx(stream)

while True:
	time.sleep(5)
#while stream.is_active():
#	time.sleep(20)
#	stream.stop_stream()
#	print("done")

stream.close()
p.terminate()
