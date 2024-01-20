# Escriba un programa que muestre una tabla de multiplicar como la siguiente:
def generate_multiplication_table(n):
    # Crear la tabla de multiplicar
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:5d}", end="")
        print()

def main():
    n = int(input("Ingrese el número de filas y columnas de la tabla de multiplicar: "))
    generate_multiplication_table(n)

if __name__ == "__main__":
    main()
    