# Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
num = int(input("Ingrese el numero del cual desea sacar las potencias: "))
cant_pot = int(input("Ingrese la cantidad de potencias que desea sacar: "))
potencias = list()
for i in range(cant_pot):
    potencia = num**(i+1)
    potencias.append(potencia)

print(f"\n\t {potencias}")
    
