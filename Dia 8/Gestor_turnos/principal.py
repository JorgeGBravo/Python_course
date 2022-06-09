from generadores_numeros import *
from os import system


def inicio():
    status = True

    while status:
        system('cls')
        print('Bienvenido a su Farmacia')
        print('''     Eliga su turno''')
        print()
        print('    [P] - Perfumeria')
        print('    [F] - Farmacia')
        print('    [C] - Cosmetica')

        try:
            valor = input().upper()
            ['P', 'F', 'C', 'Q'].index(valor)

        except ValueError:
            system('cls')
            print('Esa opción no es valida')
            input('Pulse una tecla para continuar')
        else:
            if valor == 'Q':
                status = False
                continue
            ticket(valor)



inicio()