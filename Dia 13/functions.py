import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import wikipedia
import datetime
from wallet import wallet
from languages import *

var_language = language_control()
'''
# know what voices are in the system


engine = pyttsx3.init()

for idiom in engine.getProperty('voices'):
    print(idiom)
'''


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


def youTube_browser():
    webbrowser.open('https://www.youtube.com/')


def google_browser():
    webbrowser.open('https://www.google.com')


def pywhatkit_search(search):
    pywhatkit.search(search)


def wiki_search(search):
    if language.lower() == 'spanish':
        speak('Buscando...')
        wikipedia.set_lang('es')
        result = wikipedia.summary(search, sentences=1)
        speak('Esto es lo que he encontrado...')
    else:
        speak('Searching...')
        wikipedia.set_lang('en')
        result = wikipedia.summary(search, sentences=1)
        speak('This is what I found...')

    speak(result)


def play_search(search):
    pywhatkit.playonyt(search)


def play_joke():
    if language.lower() == 'spanish':
        speak(pyjokes.get_joke('es'))
    else:
        speak(pyjokes.get_joke('en'))


def financial_information():
    speak_what_are_you_looking_for()
    count = False
    condition = True
    while condition:
        print('en iformacion')
        speak_repeat_what_you_are_looking(count)
        search = change_audio_as_text()
        print(search)
        split_0 = search.split(' ')[0]
        split_1 = search.split(' ')[1]
        if language.lower() == 'spanish':
            if split_0 == 'precio':
                try:
                    search_action = wallet[split_1]
                    search_valor = yf.Ticker(search_action)
                    actual_price = search_valor.info['regularMarketPrice']
                    speak(f'El precio actual de {split_1} es {actual_price}')
                    speak(f'El ultimo titular es: {search_valor.news[0]["title"]}')
                    condition = False

                except:
                    count = True
                    speak('No he encontrado lo que andas buscando')
                    continue

        else:
            if split_1 == 'price':
                try:
                    search_action = wallet[split_0]
                    search_valor = yf.Ticker(search_action)
                    actual_price = search_valor.info['regularMarketPrice']
                    speak(f'The current price of {split_0} is {actual_price}')
                    speak(f'the latest headline is: {search_valor.news[0]["title"]}')
                    condition = False

                except:
                    count = True
                    speak("I can't find what you were looking for")
                    continue
