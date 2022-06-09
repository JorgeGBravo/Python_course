from pathlib import Path, PureWindowsPath


carpeta = Path("C:/Users/jdgbr/PycharmProjects/pythonCourse/otras_cosas")

carpeta_windows = PureWindowsPath(carpeta)
print(carpeta_windows)

texto = carpeta / "texto.txt"
registro = carpeta / "registro.txt"

print(texto.read_text())

print(registro.exists())

if not registro.exists():
    print("no existe")
else:
    print("existe")


base = Path.home()
print(base)

carpeta_2 = Path(base, 'PycharmProjects', 'pythonCourse', 'otras_cosas')

print(carpeta_2)

#construccion de otra truta con una anterior

carpeta_3 = carpeta_2.with_name('nueva_ruta.txt')
print(carpeta_3)

#devuelve el directorio antecesor

print(carpeta_3.parent)
print(carpeta_3.parent.parent)
print(carpeta_3.parent.parent.parent)

#bucar en el Path

carpeta_down = Path(Path.home(),"Downloads")

#Para un carpeta determinada
#for txt in Path(carpeta_glob).glob("*.pdf"):
#    print(txt)

#Para la carpeta y subcarpetas

carpeta_glob = Path(Path.home())

for txt in Path(carpeta_glob).glob("**/*.txt"):
    print('hola')
    print(txt)
