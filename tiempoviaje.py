# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
tramo1 = 0
tramo2 = 0
tramo3 = 0
tiempo_total=0  

while tramo1 == 0:
    tramo1 = int(input("Duracion tramo : "))
    tramo2 = int(input("Duracion tramo: "))
    tramo3 = int(input("Duracion tramo: "))
    tiempo_total = tramo1 + tramo2 + tramo3
horas = tiempo_total//60
minutos = tiempo_total %60
print("Tiempo total de viaje: ", horas, ":", minutos)

    