import pyaudio
import wave
import sys
import math
import random

PyAudio = pyaudio.PyAudio

def playTone(bitRate,freq,time):
    numOfFrames = int(bitRate * time)
    restFrames = numOfFrames % bitRate
    waveData = ''    

    for x in xrange(numOfFrames):
     waveData = waveData+chr(int(math.sin(x/((bitRate/freq)/math.pi))*127+128))    

    #fill remainder of frameset with silence
    for x in xrange(restFrames): 
     waveData = waveData+chr(128)

    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1), 
                    channels = 1, 
                    rate = bitRate, 
                    output = True)
    stream.write(waveData)
    stream.stop_stream()
    stream.close()
    p.terminate()