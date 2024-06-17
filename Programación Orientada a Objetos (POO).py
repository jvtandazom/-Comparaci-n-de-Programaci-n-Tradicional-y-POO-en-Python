#  Comparación de Programación Tradicional y POO en Python

#Programación Tradicional: Se basa en funciones que encapsulan operaciones y datos, adecuada para tareas simples y
# lineales POO:
#Utiliza clases y objetos para modelar datos y operaciones relacionadas, promoviendo la reutilización del código y una
# organización más estructurada.


# Programación Orientada a Objetos (POO)
class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas_diarias(self):
        """ Método para ingresar las temperaturas diarias """
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        """ Método para calcular el promedio semanal """
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio

# Programa principal
def main_poo():
    print("Programación Orientada a Objetos (POO) - Promedio Semanal del Clima\n")
    clima = ClimaDiario()
    clima.ingresar_temperaturas_diarias()
    promedio = clima.calcular_promedio_semanal()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}")

# Ejecución del programa
if __name__ == "__main__":
    main_poo()