import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Idioms
idSpanish = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
idEnglish = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


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
    engine.setProperty('voice', idEnglish)
    # pronounce message
    engine.say(message)
    engine.runAndWait()


'''
# know what voices are in the system


engine = pyttsx3.init()

for idiom in engine.getProperty('voices'):
    print(idiom)
'''


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


def time_now():
    # var whit data of hour
    date_time = datetime.datetime.now()
    hour = f'The time is {date_time.hour} hour and {date_time.minute} minute'

    speak(hour)


def initial_greeting():
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        moment = 'Good night'
    elif hour.hour >= 6 and hour.hour < 13:
        moment = 'Good Morning'
    else:
        moment = 'Good evening'

    speak(f'{moment}, I´m Helena, your personal assistant. Tell me where I can help you')


def ask_for_things():
    initial_greeting()

    init = True
    while init:
        # Active mic
        order = change_audio_as_text()

        if 'open YouTube' in order:
            speak('I´m will open youtube for you')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'open browser' in order:
            webbrowser.open('https://www.google.com')
            continue


ask_for_things()

