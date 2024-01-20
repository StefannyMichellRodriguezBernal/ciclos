# Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
Largo=int(input('Lado: '))
Longitud_final= Largo + 2*(Largo-1)
for i in range(Largo):
    cadena_final=''
    for j in range(Largo+2*i):
        cadena_final+='*'
    print(cadena_final.center(Longitud_final))
for x in range(1,Largo):
    cadena_final=''
    for j in range(2,Largo+2*(Largo-x),1):
        cadena_final+='*'
    print(cadena_final.center(Longitud_final))
    