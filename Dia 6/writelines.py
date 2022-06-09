registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

texto = open("registro.txt","a")

for line in registro_ultima_sesion:
    texto.writelines(line + "\t")

texto.close()

texto = open("registro.txt")
print(texto.read())