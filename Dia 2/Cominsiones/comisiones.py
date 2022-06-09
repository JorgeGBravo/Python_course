nombre = input("Nombre: ")
ventas = float(input("Cantidad Ventas: "))
porcentaje = 13
comision = round(ventas * porcentaje/100, 2)

print(f"La comision de {nombre} es de {comision} Euros")


