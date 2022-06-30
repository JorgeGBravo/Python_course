import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Listen mic and devolver audio as text
def change_audio_as_text():
    # save recognizer in var
    r = sr.Recognizer()

    # config mic
    with sr.Microphone() as origen:
        # time to pause
        r.pause_threshold = 0.8
        # inform init the recorder
        print('Start talking...')
        # save the audio
        audio = r.listen(origen)

    try:
        # search in google as text
        order = r.recognize_google(audio, language='es-ES')
        # test ok
        print('Said: ' + order)
        return order
    except sr.UnknownValueError:
        # test no ok
        print('No understand')
        return 'Not found'
    except sr.RequestError:
        # test no ok
        print('There is no service')
        return 'There is no service'
    except:
        print('It could not be')
        return 'It could not be'


# assistant speak
def speak(message):
    # Turn on engine pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', idSpanish)
    # pronounce message
    engine.say(message)
    engine.runAndWait()


'''
# know what voices are in the system


engine = pyttsx3.init()

for idiom in engine.getProperty('voices'):
    print(idiom)
'''
# Idioms
idSpanish = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
idEnglish = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

def get_day():
    day = datetime.date.today()
    print(day)
    week_day = day.weekday()
    print(week_day)

    # dic with name of days
    calendar = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}

    # say day of week
    speak(f'Today is {calendar[week_day]}')

get_day()