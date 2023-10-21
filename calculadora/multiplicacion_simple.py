def is_number(value):
    """Verifica si el valor es un número."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def multiplicar(num1, num2):
    # Escenario de error: Alguna de las entradas no es un número
    if not is_number(num1) or not is_number(num2):
        raise ValueError("Error: Alguna de las entradas no es un número.")
    
    # Convertimos los argumentos a flotantes
    n1 = float(num1)
    n2 = float(num2)
    
    # Realizamos la multiplicación
    resultado = n1 * n2
    return float(resultado)  # Aseguramos que el resultado sea decimal

def probar_multiplicacion():
    def prueba(num1, num2, esperado):
        try:
            resultado = multiplicar(num1, num2)
            if resultado == esperado:
                print(f"Prueba exitosa: {num1} * {num2} = {esperado}")
            else:
                print(f"Error en prueba: {num1} * {num2}. Se esperaba {esperado} pero se obtuvo {resultado}")
        except ValueError as e:
            print(f"Error en prueba: {num1} * {num2}. {e}")
    
    # Casos de prueba
    prueba("5", "3", 15.0)
    prueba("4.2", "2", 8.4)
    prueba("0", "3", 0.0)
    prueba("3", "0", 0.0)
    prueba("-2", "3", -6.0)
    prueba("2", "-3", -6.0)
    prueba("-2", "-3", 6.0)
    # Escenario de error: Alguna de las entradas no es un número
    prueba("hola", "3", None)  
    prueba("5.2.3", "3", None)

if __name__ == "__main__":
    # Entrada del usuario
    while True:
        num1 = input("Ingresa el primer número (o 'salir' para terminar): ")
        if num1.lower() == 'salir':
            break
        num2 = input("Ingresa el segundo número: ")

        try:
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {resultado}\n")
        except ValueError as e:
            print(f"{e}\n")
    
    # Realizamos las pruebas
    print("\nEjecutando pruebas unitarias...\n")
    probar_multiplicacion()
