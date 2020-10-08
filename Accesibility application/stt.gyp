import io
import os

# Imports the Google Cloud client library
from google.cloud import speech_v1 as speech

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'demo_1.flac')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config,audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    text_file = open("Output.txt", "w")
    text_file.write('Transcript: {}'.format(result.alternatives[0].transcript))
    text_file.close()