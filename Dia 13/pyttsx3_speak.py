import pyttsx3

idSpanish = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
idEnglish = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


def speak(message):
    # Turn on engine pyttsx3
    engine = pyttsx3.init()
    # set language voice
    engine.setProperty('voice', idEnglish)
    # pronounce message
    engine.say(message)
    engine.runAndWait()