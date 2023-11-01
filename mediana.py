from calculosestadisticos import CalculosEstadisticos
#para calcular la mediana importamos median de numpy
from numpy import median
import pandas as pd

#ConcreteProductA3

class Mediana(CalculosEstadisticos):
    def calcular(self, datos: int ) -> float:
        # Leer el archivo CSV utilizando pandas
        df = pd.read_csv('emergencias.csv')

        # Mostrar las opciones disponibles al usuario
        print("Opciones disponibles:")
        print("1. FECHA_NUM")
        print("2. ID-EVENTO")

        # Solicitar al usuario que ingrese el número de la opción deseada
        opcion = int(input("Ingrese el número de la opción que desea utilizar: "))

        # Verificar si la opción ingresada por el usuario es válida
        if opcion == 1:
            columna_seleccionada = 'FECHA_NUM'
        elif opcion == 2:
            columna_seleccionada = 'ID-EVENTO'
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
            return

        # Obtener los datos de la columna seleccionada
        datos = df[columna_seleccionada]

        return median(datos)

