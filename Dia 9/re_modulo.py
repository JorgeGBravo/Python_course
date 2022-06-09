import re


def verificar_email(email):
    expresion = r'\w+@\w+[.]com'
    if re.match(expresion, email) is not None:
        print('OK')
    else:
        print('No')


##verificar_email('djñajdñal@gmail.co')


def verificar_saludo(frase):
    expresion = r'Hola'
    if re.search(expresion, frase) is not None:
        print('Ok')
    else:
        print('No has saludado')

verificar_saludo('Hola Como estás')