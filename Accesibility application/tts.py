import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voices = engine.getProperty('voices') 

engine.setProperty('voice', voices[0].id) #Male
#engine.setProperty('voice', voices[1].id) #Female

print (rate)
print (volume)

text_file = open("/Users/Lookeaw1/Output.txt", 'r')
transcript = str(text_file.read())

while True:
    engine.say(transcript)
    engine.runAndWait()

    break

"""
engine.say("Hello! Please input text you want me to speak!")
engine.runAndWait()


while True:
    print("Please input the text you wishes to speaks.")
    inputText = input()

    engine.say(inputText)
    engine.runAndWait()
"""