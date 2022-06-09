def registro_error(archivo):
    logs = open(archivo, "a")
    logs.write("se ha registrado un error de ejecución")
    logs.close()


registro_error("texto.txt")