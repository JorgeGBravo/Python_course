import pyttsx3

def speak(message):
    # Turn on engine pyttsx3
    engine = pyttsx3.init()
    # pronounce message
    engine.say(message)
    engine.runAndWait()