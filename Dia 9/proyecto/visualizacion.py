import os
from io import open
import textwrap

path = os.getcwd()
carpeta_extraccion = path + '\\extraccion'
print(carpeta_extraccion)
archivos_directorio = os.listdir(carpeta_extraccion)
print(archivos_directorio)

archivo = open(carpeta_extraccion + '\\Instrucciones.txt', 'r', encoding="utf-8")

texto = archivo.read()
print(texto)
print(textwrap.fill(texto, width=100))

archivo.close()