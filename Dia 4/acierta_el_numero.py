from random import randint

nombre = input("Dime tu numbre : ")
numero_input = int(input(f"Hola {nombre}, dime un número del 1 al 100, ¿en cual piensas? : "))
numero_random = randint(0 ,101)
counter = 0

while counter < 8:
    if numero_input == '':
        numero_input = int(input(f"Dime otro número : "))

    if numero_input not in range(0,101):
        print("El numero introducido no está dentro del rango estipulado\n")
    counter += 1

    if numero_input > numero_random:
        print(f"{nombre.capitalize()}, tu numero en mayor, te quedan {8 - counter} intentos")
        numero_input = ''

    elif numero_input < numero_random:
        print(f"{nombre.capitalize()}, tu numero en menor, te quedan {8 - counter} intentos")
        numero_input = ''

    else:
        print(f"Enhorabuena!!!!! el {numero_random} es el numero.")
        break

if counter == 8:
    print(f"Has perdido el numero a acertar era el {numero_random}")