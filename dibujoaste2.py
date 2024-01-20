# Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:
def triangulo_dibujo(Altura):
    for i in range(1, Altura + 1):
        print('*' * i)
def main():
    try:
        Altura = int(input("Altura: "))      
        if Altura > 0:
            triangulo_dibujo(Altura)
        else:
            print("INgrese un valor mayor de cero")
    except ValueError:
             print("Ingrese un valor numerico")
if __name__ == "__main__":
     main()
