USA = 900
CANADA = 800
EUROPA = 950
RESTO = 1250

destino = input("ingrese al destino al que desea llamar: ")
tiempo = int(input("ingrese el tiempo de la llamada: "))

descuento = (tiempo*0.20)

if tiempo > 15:
    tiempo = descuento-tiempo

if destino == "estados unidos":
    print("el costo de la llamada es: ", USA * tiempo)
elif destino == "canada":
    print("el costo de la llamada es: ", CANADA*tiempo)
elif destino == "europa":
    print("el costo de la llamada es: ", EUROPA*tiempo)
elif destino == "resto del mundo":
    print("el costo de la llamada es:", RESTO*tiempo)
else:
    print("destino invalido")
