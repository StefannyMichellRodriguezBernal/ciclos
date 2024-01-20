# Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:
Numero = int(input('n: '))
Suma = 0
for i in range(Numero):
    Suma+=(-1)**(i)*(1/(2*i+1))
pi = 4 * Suma
print(pi)
