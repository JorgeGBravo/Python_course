def devolver_distintos(*args):
    suma = 0
    indice_maximo = args.index(max(args))
    indice_minimo = args.index(min(args))
    indice_intermedio = None

    for num in args:
        suma += num

    for indice in [0,1,2]:
        if indice == indice_maximo:
            pass
        elif indice == indice_minimo:
            pass
        else:
            indice_intermedio = indice
    if suma > 15:
        return max(args)
        #devuelve el numero mayor
    elif suma < 10:
        return min(args)
        #devuelve el numero menor
    elif 10 <= suma <= 15:
        return args[indice_intermedio]
        #devuelve el numero intermedio

args = [6, 5 ,4]

print(devolver_distintos(*args))

def devolver_distintos_B(a,b,c):
    suma = a+b+c
    lista = [a,b,c]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos_B(6,5,4))