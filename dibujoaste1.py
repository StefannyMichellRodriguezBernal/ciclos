# Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:
Altura = int(input('Altura:'))
Ancho= int(input('Ancho: '))

for i in range(Altura):
    for j in range(Ancho):
        print('*', end='')
    print()