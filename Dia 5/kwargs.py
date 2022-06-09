def prueba(num1, num2, *args, **kwargs):

    print(f"el primer num es {num1}")
    print(f"el segundo num es {num2}")

    for arg in args:
        print(f"contenido de args {arg}")

    for key, value in kwargs.items(): # ojo con el items()
        print(f"{key} = {value}")


args = [100, 200, 300, 400]
kwargs ={"x":10, "y":"veinte", "z":'30'}

prueba(10,20, *args, **kwargs)


def lista_atributos(**kwargs):
    lista = []
    for key, value in kwargs.items():
        lista.append(value)
    return lista

def cantidad_atributos(**kwargs):
    count = 0
    for key in kwargs:
        count += 1
    return count

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")