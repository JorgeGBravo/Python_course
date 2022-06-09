def letras_en_orden(palabra):
    letras = []
    for letra in palabra:
        if letra not in letras:
            letras.append(letra)
        else:
            pass
    print(sorted(letras))


letras_en_orden("holaaooooooohita")


def letras_orden(palabra):
    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)

    '''mi_lista = list(mi_set)
        mi_lista.sort()'''

    print(sorted(mi_set))

letras_orden("holaaooooooohita")
