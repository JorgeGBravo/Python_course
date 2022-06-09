'''from random import choice


def lanzar_dados():
    dado = [1 , 2 , 3 , 4 , 5 , 6]
    dado_A = choice(dado)
    dado_B = choice(dado)
    return dado_A , dado_B


jugada = lanzar_dados()


def evaluar_jugada(jugada):
    uno , dos = jugada
    suma = uno + dos

    if suma <= 6:
        print(f"La suma de tus dados es {suma}. Lamentable")
    elif 6 < suma < 10:
        print(f"La suma de tus dados es {suma}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma}. Parece una buena jugada")


evaluar_jugada(jugada)'''

from random import choice


def lanzar_dados():
    dado = [1 , 2 , 3 , 4 , 5 , 6]
    lanzamiento = choice(dado)
    return int(lanzamiento)


jugada_1 = lanzar_dados()
jugada_2 = lanzar_dados()

def evaluar_jugada(jugada_1 , jugada_2):
    suma = jugada_1 + jugada_2

    if suma <= 6:
        return (f"La suma de tus dados es {suma}. Lamentable")
    elif 6 < suma < 10:
        return (f"La suma de tus dados es {suma}. Tienes buenas chances")
    else:
        return (f"La suma de tus dados es {suma}. Parece una buena jugada")


print(evaluar_jugada(jugada_1 , jugada_2))