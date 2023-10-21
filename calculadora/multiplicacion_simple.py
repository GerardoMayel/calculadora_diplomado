def multiplicar(a, b):
    return a * b

def main():
    try:
        # Solicitar al usuario que ingrese dos números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Calcular y mostrar el resultado
        resultado = multiplicar(num1, num2)
        print(f"El resultado de {num1} multiplicado por {num2} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
