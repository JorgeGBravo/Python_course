import random
from os import system

class Persona:

    def __init__(self , nombre , apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, cuenta, balance):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance


    def __str__(self):
        print(f'''Nombre:     {self.nombre}
Apellido:   {self.apellido}
CC:         {self.cuenta}
Balance:    {self.balance}''')

    def depositar(self, cantidad):
        self.balance = self.balance + cantidad
        print(f'''Tu balance actual es = {round(self.balance, 3)}''')

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print(f'''No puedes realizar la operacion tu balance actual es {round(self.balance, 3)}''')
        else:
            self.balance = self.balance - cantidad
            print(f'''Tu balance actual es = {round(self.balance, 3)}''')

    def saldo(self):
        print(self.balance)


def cc():
    digit2 = str(random.randint(1, 25))
    digit4 = str(random.randint(1, 9999))
    digit10 = str(random.randint(1, 9999999999))
    return 'ES' + digit2 + ' ' + digit4 + ' ' + digit4 + ' ' + digit2 + ' ' + digit10




def generar():
    system('cls')
    error = False
    while not error:
        print('Creacion de Cuenta')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        balance = input('Introducir balance inicial: ')
        try:
            balance = float(balance)
            cuenta = cc()
            nuevo_cliente = Cliente(nombre, apellido, cuenta, balance)
            print(nombre.__str__())
            error = True
            return nuevo_cliente
        except ValueError:
            print("El valor del Balance parece no ser numerico")

def ingresar_cliente():
    nombre = input('Nombre del cliente: ')
    value = float(input('Importe: '))
    nombre.depositar(value)
    return nombre.saldo()


def retirar_cliente(nombre, value):
    nombre = input('Nombre del cliente: ')
    value = input('Importe: ')
    nombre.retirar(value)
    return nombre.saldo()



def gestion_cuenta():
    opcion = 'x'
    while not opcion.isnumeric() or int(opcion) not in range(1 , 4):
        print('Gestion de Cuenta')
        print('[1] - Ingresar \n'
              '[2] - Retirar \n'
              '[3] - Volver \n')
        opcion = input()
    return int(opcion)


def inicio():
    opcion = 'x'
    while not opcion.isnumeric() or int(opcion) not in range(1, 4):
        print('Gestion de Cuentas')
        print('[1] - Crear Cuenta \n'
              '[2] - Gestionar Cuenta \n'
              '[3] - Salir \n')
        opcion = input()
    return int(opcion)




finalizar_programa = False

while not finalizar_programa:

    menu = inicio()
    if menu == 1:
        generar()
    elif menu == 2:
        opcion = gestion_cuenta()
        if opcion == 1:
            ingresar_cliente()
        elif opcion == 2:
            retirar_cliente()
        elif opcion == 3:
            pass
    elif menu == 3:
        finalizar_programa = True

