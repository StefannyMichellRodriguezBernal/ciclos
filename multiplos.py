# Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:
def show_multiplication_table(numero):
    print(f"Tabla de multiplicar del {numero}:")

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    show_multiplication_table(numero)

if __name__ == "__main__":
    main()
    