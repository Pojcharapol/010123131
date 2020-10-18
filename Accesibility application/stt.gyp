import io
import os
import sys

#Microphone library

import pyaudio
import wave

#language initialisation
print ('\n')
print ('Please select language choice:')
print ('English (US): 1 (Default)')
print ('English (UK): 2')
print ('Thai: 3')
print ('Japanese: 4')
print ('Others: 5')

try:
    choice_select = int(input('Selected: '))

    if choice_select == int(1):
        lang = ('en-US')

    elif choice_select == int(2):
        lang = ('en-GB')

    elif choice_select == int(3):
        lang = ('th-TH')

    elif choice_select == int(4):
        lang = ('ja-JP')

    elif choice_select == int(5):
        lang = input('Please insert language code: ')

    else:
        lang = ('en-US')

except:
       
    print ("Please select one language!")
    
    os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)

#Microphone area
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "/Users/Lookeaw1/Desktop/output2.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("\n")
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
wave_name = "output.wav"
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
    language_code=lang,
    enable_automatic_punctuation = True,
    enable_word_time_offsets = True)

# Detects speech in the audio file
response = client.recognize(config = config ,audio = audio)

for result in response.results:

    print ('\n')
    print('Transcript: {}'.format(result.alternatives[0].transcript))

    conf = (result.alternatives[0].confidence) * 100

    print ('Confidence: {} %'.format(conf)) 
    print ('\n')

    for word_info in result.alternatives[0].words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            print(
                f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}"
            )

    if conf < 80:
        print ('\n')
        print ('Caution: I am not sure about the transcribed message! please try speak again more clearly!')
    
    text_file = open("Output.txt", "a+")
    speech_out = open("speech.txt", "w")
    
    text_file.write('Transcript: {} \r\n'.format(result.alternatives[0].transcript))
    text_file.write('Confidence: {} %\r\n'.format(conf))
    
    speech_out.write('{}'.format(result.alternatives[0].transcript))
    
    text_file.close()
    speech_out.close()