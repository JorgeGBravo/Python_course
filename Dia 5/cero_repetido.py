def repetido(*args):
    last_numero = None
    for numero in args:
        if last_numero == 0 and numero == 0:
            return True
        else:
            last_numero = numero
    return False


args = (0,0,3,0,2,3,4,5,0)

print(repetido(*args))

def ceros_vecinos(*args):
    contador = 0

    for num in args:
        if contador +1 == len(args):
            return False
        elif args[contador] == 0 and args[contador +1] == 0:
            return True
        else:
            contador += 1
    
    return False

print(ceros_vecinos(*args))