from random import choice


def palabra():
    palabras = ["platano", "papi", "chocolate", "cartas", "rollo", "mandarina", "portatil",
                "pizarra", "coche", "puerta", "heroina", "casa", "pared", "tornillo",
                "bebida", "fiesta", "manzana", "tornillo", "bolso", "movil"]
    return choice(palabras)


def match_count(count):
    match (count):
        case 5:
            print('''                         O''')
            print(f"La palabra no contine la letra {letra} te quedan {count} intentos")
        case 4:
            print('''                         O
                         |''')
            print(f"La palabra no contine la letra {letra} te quedan {count} intentos")
        case 3:
            print('''                         O
                        -|''')
            print(f"La palabra no contine la letra {letra} te quedan {count} intentos")
        case 2:
            print('''                         O
                        -|-''')
            print(f"La palabra no contine la letra {letra} te quedan {count} intentos")
        case 1:
            print('''                         O
                        -|-
                        /''')
            print(f"La palabra no contine la letra {letra} te quedan {count} intento")

        case _:
            print('''                         O
                        -|-
                        / \ ''')
            print("Estás ahorcado !!!")
            exit()


def is_letra(palabra):

    letras_comprobacion = 'abcdefghijklmnñopqrstuvwxyz'
    comprobacion = False
    while not comprobacion:
        letra = input("Escribe una letra: ").lower()
        if letra in letras_comprobacion and len(letra) == 1:
            comprobacion = True
            return letra
        elif len(letra) != 2 and letra == palabra:
            print(f"Enhorabuena has acertado. La palabra es -' {palabra.capitalize()} '- ")
            exit()
        else:
            print("Por favor introduce una letra del alfabeto.")
            continue


def print_palabra_guiones(palabra):
    for letra in palabra:
        print("-", end=" ")
    print("\n")


def print_acierto_guiones(palabra, set_palabra):
    if len(set_palabra) != len(set(palabra)):
        for l in palabra:
            if l in set_palabra:
                print(l, end=" ")
                pass
            else:
                print("-", end=" ")
                pass
    else:
        print(f"Enhorabuena has ganado. La palabra es -' {palabra.capitalize()} '- ")
        exit()


palabra = palabra()
print_palabra_guiones(palabra)
letras_list = list(palabra)
count = 6
set_palabra = set()
while count <= 6:
    letra = is_letra(palabra)
    if letra not in letras_list:
        count -= 1
        match_count(count)
    else:
        if letra not in set_palabra:
            set_palabra.add(letra)
            print_acierto_guiones(palabra, set_palabra)
        else:
            print("Letra ya introducida anteriormente")
            pass