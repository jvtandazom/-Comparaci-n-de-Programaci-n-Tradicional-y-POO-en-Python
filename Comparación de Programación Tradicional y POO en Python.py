# Programación Tradicional - Funciones

def ingresar_temperaturas_diarias():
    """ Función para ingresar las temperaturas diarias """
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """ Función para calcular el promedio semanal """
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Programa principal
def main_tradicional():
    print("Programación Tradicional - Promedio Semanal del Clima\n")
    temperaturas = ingresar_temperaturas_diarias()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}")

# Ejecución del programa
if __name__ == "__main__":
    main_tradicional()



