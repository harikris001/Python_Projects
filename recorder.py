#install sounddevice package using pip install
import sounddevice
from scipy.io.wavfile import write

#sampling rate
fs =44100
seconds = int(input("Enter the durtion of the recording: "))

print("Recording Started.....")
record_voice = sounddevice.rec(int(seconds*fs),samplerate = fs.channels=2)
sounddevice.wait()
write("audioout.wav",fs,record_voice)
print("Finished Recording....")
