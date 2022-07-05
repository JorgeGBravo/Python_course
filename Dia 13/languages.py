from config import language
import datetime

english = 'en-GB'
english_language = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
spanish = 'es-ES'
spanish_language = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'


def language_control():
    if language.lower() == 'english':
        language_recognize = english
        language_speak = english_language
        return [language_recognize, language_speak]

    elif language.lower() == 'spanish':
        language_recognize = spanish
        language_speak = spanish_language
        return [language_recognize, language_speak]

    else:
        language_recognize = english
        language_speak = english_language
        return [language_recognize, language_speak]


def spanish_as_for_things():
    init = True
    while init:
        # Active mic
        order = change_audio_as_text()
        print(f'en order: {order}')
        split_order = order.split(' ')

        if 'abrir' in split_order[0]:
            if 'YouTube' in split_order[1]:
                speak('Estoy abriendo YouTube para ti')
                youTube_browser()
                continue
            elif 'navegador' in split_order[1]:
                google_browser()
                continue

        elif 'buscar' in split_order[0]:
            speak('Estoy buscado para ti')
            search = order.split(' ', 1)[1]
            # search = order.replace('search', '')
            pywhatkit_search(search)
            continue

        elif '¿Qué hora és?' in order:
            time_now()
            continue

        elif 'qué es' in order:
            search = order.split('qué es', 1)[1]
            wiki_search(search)
            continue

        elif 'YouTube' in split_order[0]:
            speak('Buena idea, ya te lo reproduzco')
            search = order.split('YouTube', 1)[1]
            play_search(search)
            continue

        elif 'dime un chiste' in order:
            play_joke()
            continue

        elif 'información financiera' in order:
            financial_information()
            continue

        elif 'hasta luego' or 'adios' or 'nos vemos' in order:
            speak('Nos vemos, cualquier cosa que necesites me avisas')
            break

def english_as_for_things():
    init = True
    while init:
        # Active mic
        order = change_audio_as_text()
        print(f'en order: {order}')
        split_order = order.split(' ')

        if 'open' in split_order[0]:
            if 'YouTube' in split_order[1]:
                speak('I´m will open youtube for you')
                youTube_browser()
                continue
            elif 'browser' in split_order[1]:
                google_browser()
                continue

        elif 'search' in split_order[0]:
            speak('I´m looking for you')
            search = order.split(' ', 1)[1]
            # search = order.replace('search', '')
            pywhatkit_search(search)
            continue

        elif 'what time is it' in order:
            time_now()
            continue

        elif 'what is' in order:
            search = order.split('what is', 1)[1]
            wiki_search(search)
            continue

        elif 'play' in split_order[0]:
            speak('Good idea, i start to play it')
            search = order.split('play', 1)[1]
            play_search(search)
            continue

        elif 'Tell me a joke' in order:
            play_joke()
            continue

        elif 'financial information' in order:
            financial_information()
            continue

        elif 'bye' or 'goodbye' or 'see you' in order:
            speak('See you, anything you need let me know')
            break


def speak_day(week_day):
    if language.lower() == 'english':
        calendar = {0: 'Monday',
                    1: 'Tuesday',
                    2: 'Wednesday',
                    3: 'Thursday',
                    4: 'Friday',
                    5: 'Saturday',
                    6: 'Sunday'}
        return f'Today is {calendar[week_day]}'

    elif language.lower() == 'spanish':
        calendar = {0: 'Lunes',
                    1: 'Martes',
                    2: 'Miércoles',
                    3: 'Jueves',
                    4: 'Viernes',
                    5: 'Sábado',
                    6: 'Domingo'}
        return f'Today is {calendar[week_day]}'


def hour(date_time):
    if language.lower() == 'english':
        return f'The time is {date_time.hour} hour and {date_time.minute} minute'
    elif language.lower() == 'spanish':
        return f'La hora es {date_time.hour} horas y {date_time.minute} minutos'


def initial_greeting():
    hour = datetime.datetime.now()
    if language.lower() == 'spanish':
        if hour.hour < 6 or hour.hour > 20:
            moment = 'Buenos dias'
        elif hour.hour >= 6 and hour.hour < 13:
            moment = 'Buenos dias'
        else:
            moment = 'Buenas tardes'

        return f'{moment}, Soy Helena, tu asistente personal. Dime en que te puedo ayudar'

    else:
        if hour.hour < 6 or hour.hour > 20:
            moment = 'Good night'
        elif hour.hour < 13 and hour.hour >= 6:
            moment = 'Good morning'
        else:
            moment = 'Good evening'

        return f'{moment}, I´m Zira, your personal assistant. Tell me where I can help you'


def speak_repeat_what_you_are_looking(count):
    if language.lower() == 'spanish':
        if count:
            speak('Sigo sin entenderte')
        speak('Por favor, puedes decirme de nuevo lo que buscas')
    else:
        if count:
            speak('I still do not understand you')
        speak('Please can you tell me again what you are looking for')

def speak_what_are_you_looking_for():
    if language.lower() == 'spanish':
        speak('¿Dime lo que buscas?')
    else:
        speak('Tell me what you are looking for')

from functions import *
