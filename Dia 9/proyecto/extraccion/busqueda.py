import os
from io import open
import re
import datetime
import timeit
import math

directorio = os.getcwd() + '\\Mi_Gran_Directorio'
expresion = r'N\D{3}[-]\d{5}'
hoy = datetime.date.today()
count = 0

def inicio(directorio):
    global count
    print(f'Fecha de búsqueda:\t {hoy.day}/{hoy.month}/{hoy.year}')
    print('''ARCHIVO\t\t\tNRO. SERIE \n-------\t\t\t----------''')
    init = timeit.timeit()
    busqueda(directorio)
    fin = timeit.timeit()
    total_timeit = math.ceil(init - fin)
    print()
    print(f'Números encotrados: {count}')
    print(f'Duración de la busqueda:{total_timeit}')

def busqueda(directorio):
    global count
    for directorio, subdirectorio, ficheros in os.walk(directorio):
        for fichero in ficheros:
            var = os.path.join(directorio, fichero)
            x = open(var)
            find = re.search(expresion, x.read())
            if find is not None:
                print(f'{fichero}\t{find.group(0)}')
                count += 1
            x.close()

inicio(directorio)