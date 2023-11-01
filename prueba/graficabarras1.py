from graficas1 import Graficas
import pandas as pd
import matplotlib.pyplot as plt

# concreteProductB1

class GraficaBarras(Graficas):
    def grafica(self) -> None:
        data = pd.read_csv('emergencias.csv')
        data['FECHA'] = pd.to_datetime(data['FECHA'], errors='coerce')
        # Agrupar por fecha y contar las activaciones por día
        activaciones_por_dia = data.groupby(data['FECHA'].dt.date).size()

        # Visualizar el número de activaciones por día
        activaciones_por_dia.plot(kind='bar', figsize=(10, 6))
        plt.xlabel('Fecha')
        plt.ylabel('Número de Activaciones')
        plt.title('Número de Activaciones por Día')
        plt.show()
        # Guardar la imagen del número de activaciones por día
        plt.savefig('activaciones_por_dia.png')