import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from languages import *

var_language = language_control()


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
        order = r.recognize_google(audio, language=var_language[0])
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
    engine.setProperty('voice', var_language[1])
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
    # say day of week
    speak(speak_day(week_day))


def time_now():
    # var whit data of hour
    date_time = datetime.datetime.now()
    speak(hour(date_time))


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
        print(f'en order: {order}')
        split_order = order.split(' ')

        if 'open' in split_order[0]:
            if 'YouTube' in split_order[1]:
                speak('I´m will open youtube for you')
                webbrowser.open('https://www.youtube.com/')
                continue
            elif 'browser' in split_order[1]:
                webbrowser.open('https://www.google.com')
                continue

        elif 'search' in split_order[0]:
            speak('I´m looking for you')
            search = order.split(' ', 1)[1]
            webbrowser.open(f'https://www.google.com/search?q={search}')

        elif 'what time is it' in order:
            time_now()
            continue

        elif 'what is' in order:
            search = order.split('what is', 1)[1]
            result = wikipedia.search(search)
            print(result)
            speak(result[0])
            continue


ask_for_things()

