from languages import *


def ask_for_things():
    speak(initial_greeting())
    if language.lower() == 'spanish':
        spanish_as_for_things()
    else:
        english_as_for_things()


ask_for_things()

