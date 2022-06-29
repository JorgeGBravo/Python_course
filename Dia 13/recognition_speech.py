import speech_recognition as sr


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


change_audio_as_text()
