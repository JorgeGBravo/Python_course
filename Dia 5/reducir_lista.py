def reducir_lista(lista_numeros):
    lista_no_duplicada = []
    numero_max = max(lista_numeros)
    for numero in lista_numeros:
        if numero != numero_max:
            if numero not in lista_no_duplicada:
                lista_no_duplicada.append(numero)
    return lista_no_duplicada

lista = [1,2,15,7,2]

lista_nueva = reducir_lista(lista)
print(lista_nueva)
def promedio(lista):
    tamaño = len(lista)
    suma = 0
    for numero in lista:
        suma = suma + numero

    return suma / tamaño


print(promedio(lista_nueva))
