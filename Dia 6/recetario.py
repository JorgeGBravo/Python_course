from pathlib import Path
from os import system, remove
from shutil import rmtree

carpeta = Path(Path.home(), 'PycharmProjects', 'pythonCourse', 'Recetario', 'Recetas')
dic_recetas = {}
dic_categorias = {}


def contador_recetas():
    count = 0
    for txt in Path(carpeta).glob("**/*.txt"):
        count += 1
    return count


def inicio():
    system('cls')
    count = contador_recetas()
    dicc_recetas()
    print(f'''{'*' * 5} Hola este es tu recetario {'*' * 5}
Las recietas están en el siguiente directorio:
{carpeta}

Actualmente cuenta con {count} recetas.''')
    opcion = 'x'
    while not opcion.isnumeric() or int(opcion) not in range(1, 7):
        print('Elige una opción: ')
        print(''' 
            [1]- Leer Receta
            [2]- Crear Receta
            [3]- Leer Categoría
            [4]- Eliminar Receta
            [5]- Eliminar Categoria
            [6]- Finalizar Programa
            ''')
        opcion = input()
    return int(opcion)


def dicc_recetas():
    count = 1
    for txt in Path(carpeta).glob("**/*.txt"):
        dic_recetas[count] = txt.stem
        count += 1


def listado_recetas():
    system('cls')
    count = 1
    for txt in Path(carpeta).glob("**/*.txt"):
        print(f'''{count}-{txt.stem}''')
        dic_recetas[count] = txt.stem
        count += 1


def leer_receta():
    numero_receta = int(input('Escribre el nuemero de la receta: '))
    if numero_receta not in dic_recetas.keys():
        print('no es valido')
    for clave, valor in dic_recetas.items():
        if numero_receta == clave:
            for txt in Path(carpeta).glob("**/" + valor + ".txt"):
                archivo = open(txt)
                system('cls')
                print(archivo.read())


def existe_receta(receta):
    for txt in Path(carpeta).glob("**/" + receta + ".txt"):
        return True
    return False


def crear_receta():
    titulo = input('Nombre de la receta: ')
    receta = input('Escribe la receta a continuación: ')
    tipo = input('Categoría: ')
    if existe_receta(titulo):
        print("La receta ya existe")
        return
    ruta = Path(carpeta, tipo, titulo + ".txt")
    archivo = open(ruta, 'w')
    archivo.write(receta)
    archivo.close()
    archivo = open(ruta)
    texto = archivo.read()
    archivo.close()
    dicc_recetas()
    return texto


def listado_categorias():
    system('cls')
    count = 0
    categoria = 'x'
    for nombre_categoria in carpeta.iterdir():
        count += 1
        dic_categorias[count] = nombre_categoria.name
    while not categoria.isnumeric() or int(categoria) not in dic_categorias.keys():
        for clave, valor in dic_categorias.items():
            print(f'[{clave}]- {valor}')
        categoria = input('Introduce una categoria: ')
    return dic_categorias[int(categoria)]


def recetas_categorias(categoria):
    count = 1
    for txt in Path(carpeta).glob(categoria + "/*.txt"):
        print(f'[{count}]- {txt.stem}')
        count += 1
    leer_receta()


def eliminar_receta():
    numero_receta = input('Introduce el numero de la receta o Q para salir: ')
    if numero_receta.lower() == 'q':
        volver_inicio()
    else:
        receta = dic_recetas[int(numero_receta)]
        for txt in Path(carpeta).glob("**/" + receta + ".txt"):
            eliminacion = eliminacion_segura()
            if not eliminacion:
                remove(txt)


def eliminar_categoria():
    for clave, valor in dic_categorias.items():
        print(f'[{clave}]- {valor}')
    categoria = input('Introduce el nombre de la Categoría a eliminar: ').lower()
    print(f'Categoría a eliminar: {categoria}')
    eliminacion = eliminacion_segura()
    if not eliminacion:
        ruta = Path(carpeta, categoria)
        rmtree(ruta)


def eliminacion_segura():
    seguro = input('Eliminar S/N : ')
    if seguro == 'N':
        return True


def volver_inicio():
    volver = 'x'
    while volver != 'v':
        volver = input('\n Escribe V para seguir: ').lower()


finalizar_programa = False

while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        listado_recetas()
        leer_receta()
        volver_inicio()

    elif menu == 2:
        crear_receta()
        volver_inicio()

    elif menu == 3:
        categoria = listado_categorias()
        recetas_categorias(categoria)
        volver_inicio()

    elif menu == 4:
        listado_recetas()
        eliminar_receta()
        volver_inicio()

    elif menu == 5:
        listado_categorias()
        eliminar_categoria()
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True
