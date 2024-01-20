# Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:
# El programa debe mostrar tres columnas que contengan la siguiente información:
# El programa debe terminar cuando la fracción decimal sea menor o igual a 0.000001.
fraccion=1
contar = 1
suma=0
#hace print del cabecero para organizar la salida de los datos en las columnas
palabra = ['POTENCIA', 'FRACCIÓN', 'SUMA']
for t in palabra:
    print(t, end=' ')
print()

while fraccion>0.000001:
    fraccion=1/(2**contar)
    suma+=fraccion
    print(str(contar).ljust(8), end=' ')
    print(str(round(fraccion,4)).ljust(8), end=' ')
    print(round(suma,4))
    contar+=1