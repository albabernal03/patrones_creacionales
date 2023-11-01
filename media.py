from calculosestadisticos import CalculosEstadisticos
from numpy import mean
import pandas as pd


#ConcreteProductA1

class Media(CalculosEstadisticos):
    def calcular(self) -> float:
        # Leer el archivo CSV utilizando pandas
        df = pd.read_csv('emergencias.csv')

        # Mostrar las opciones disponibles al usuario
        print("Opciones disponibles:")
        print("1. FECHA")
        print("2. ID-EVENTO")

        # Solicitar al usuario que ingrese el número de la opción deseada
        opcion = int(input("Ingrese el número de la opción que desea utilizar: "))

        # Verificar si la opción ingresada por el usuario es válida
        if opcion == 1:
            columna_seleccionada = 'FECHA'
        elif opcion == 2:
            columna_seleccionada = 'ID-EVENTO'
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
            return

        # Obtener los datos de la columna seleccionada
        datos = df[columna_seleccionada]

        # Calcular la media utilizando numpy
        return mean(datos)
