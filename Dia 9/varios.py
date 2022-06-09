from collections import ChainMap
from collections import Counter

lista = ['libro', 'casa', 4, 33.0, 'otra' , 'casa', 33, 'var']
objeto1 = {'saludo': 'Hola', 'despedida': 'adios'}
objeto2 = {'greeting': 'Hy', 'farewell': 'bye'}

print(Counter(lista))
c = Counter(lista)
print(c['libro'])

print('*' * 10)

print(list(ChainMap(lista)))
print(list(ChainMap(objeto1)))
print(ChainMap(objeto1))
print(objeto1)

print('*' * 10)

combined = objeto1.copy()
print(combined)
combined.update(objeto2)
print(combined)

print('*' * 10)

import os

print(os.getcwd())
print(os.listdir())

print('*' * 10)

import shutil

### shutil.move()  # mover archivos de ubicación shutil.move('nombre archivo', 'ruta')

## os.unlink() # elimina un archivo en una ruta os.unlink()

import send2trash

print('*'*10)

##send2trash.send2trash() # elimina archivo y lo envia a la papelera send2trash('nombre archivo')

print('*'*10)

print(os.walk('C:\\Users\\jdgbr\\Proyectos ESM\\ProyectoESM'))

ruta = 'C:\\Users\\jdgbr\\Downloads'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {ruta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')