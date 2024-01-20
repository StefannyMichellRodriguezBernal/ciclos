# Desarrolle un programa que entregue la secuencia de Collatz de un número entero:
numero = int(input('n: '))
while numero!=1:
    print(int(numero), end=' ')
    if numero %2 == 0:
        numero /= 2
    else:
        numero = numero*3+1
print(1)
              