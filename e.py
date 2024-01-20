# Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.
import math
den=2
dif=1
e = 2
frac_ant = 1
frac = 1

while dif>0.0001:
    frac_ant = frac
    frac = 1/math.factorial(den)
    den += 1
    e += frac
    dif= frac_ant - frac
    
print(f"El aproximado de Euler es: {e}")
