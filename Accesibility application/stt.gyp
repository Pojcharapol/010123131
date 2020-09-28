import io
import os

#Microphone library
import pyaudio
import wave

#Microphone area
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "/Users/Lookeaw1/Desktop/output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# Imports the Google Cloud client library
from google.cloud import speech_v1 as speech

#change path before use
#-------------------------------------------------------------------------------
json_file = "/Users/Lookeaw1/Downloads" + "/AssistiveApplication-19801a44c25b.json"
wave_name = "demo_1.wav"
wave_file = "/Users/Lookeaw1/Desktop" + "/" + wave_name
#-------------------------------------------------------------------------------

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = wave_file

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config = config ,audio = audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    text_file = open("Output.txt", "w")
    text_file.write('Transcript: {}'.format(result.alternatives[0].transcript))
    text_file.close()