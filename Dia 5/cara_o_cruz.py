from random import *

def lanzar_moneda():
    moneda = ["Cara" , "Cruz"]
    return choice(moneda)

lista_numeros = [1,4,6,3,2]

def probar_suerte(lance, lista):
    lista = lista
    if lance != "Cara":
        print("La lista fue salvada")
        return lista
    else:
        print("La lista se autodetruirá")
        lista = []
        return lista
