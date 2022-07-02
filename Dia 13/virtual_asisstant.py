from functions import *


def ask_for_things():
    speak(initial_greeting())
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


ask_for_things()

