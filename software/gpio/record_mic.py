#this should create a wav file "testoutput.wav" and record 5 seconds from the mic
#does not play back the wav file, not real time or anything
#mostly getting used to using pyAudio

import pyaudio
import wave
import sys

#variables
CHUNK = 1024   #number of frames per buffer
RATE=44100
CHANNELS=1
FORMAT=pyaudio.paInt16
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "testoutput.wav"

#set up pyAudio and stream
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("recording...")

#reading data from stream and saving to frames
frames = []

for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
	data = stream.read(CHUNK, exception_on_overflow = False)
	frames.append(data)

print("done!")

#stop/close stream and pyaudio
stream.stop_stream()
stream.close()
p.terminate

#writing wave file
wf=wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels (CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
