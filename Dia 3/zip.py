capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

link = list(zip(paises, capitales))
for pais, capital in link:
    print(f"La capital de {pais} es {capital}")
