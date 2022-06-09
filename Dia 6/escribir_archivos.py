texto = open("mi_archivo.txt", "w")
texto.write("Nuevo texto")
texto.close()
#------------------------------------------------
texto = open("mi_archivo.txt", "r")
line = texto.readline()
print(line)
texto.close()
#------------------------------------------------
nueva_linea = ("Nuevo inicio de sesión")
texto = open("mi_archivo.txt", "a")
texto.write(nueva_linea)
texto.close()

texto = open("mi_archivo.txt", "r")
print(texto.read())
texto.close()

#------------------------------------------------
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

texto = open("resgistro.txt", "a")

for line in registro_ultima_sesion:
    texto.writelines(line + "\t")

texto.close()

texto = open("registro.txt")
print(texto.read())