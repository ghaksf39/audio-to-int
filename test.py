from scipy.io import wavfile
import scipy.io

rate, numpy_audio = wavfile.read( "sample3.wav" )
#print(rate)
for d in numpy_audio:
    print(d)