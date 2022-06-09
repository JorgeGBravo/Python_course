lista = [1,2,3,4,5]
indice = 0

for num in lista:
    print(indice , num)
    indice += 1

for indice, valor in enumerate(lista):
    print(indice, valor)

