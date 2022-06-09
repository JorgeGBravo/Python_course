lista_numeros = [1,50,502,755,34]

def cantidad_pares(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            suma = suma + numero
        else:
            pass
    return suma

print(cantidad_pares(lista_numeros))