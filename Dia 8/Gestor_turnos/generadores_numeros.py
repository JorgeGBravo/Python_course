from os import system


def generador_turno():
    valor = 0
    while True:
        if valor == 101:
            valor = 0
        valor += 1
        yield valor

numero_Perfumeria = generador_turno()
numero_Farmacia = generador_turno()
numero_Cosmetica = generador_turno()

def ticket(zona):
    system('cls')
    print(f'esta zona es {zona}')
    print('     Su turno es: ')
    if zona == 'P':
        print(f'         P-{next(numero_Perfumeria)}')
    elif zona == 'F':
        print(f'         F-{next(numero_Farmacia)}')
    elif zona == 'C':
        print(f'         C-{next(numero_Cosmetica)}')
    print('''       Espere y
     será atendido''')
    print(' ')
    input(' pulse para continuar')




