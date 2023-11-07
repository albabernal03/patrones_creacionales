from graficas import Graficas
import pandas as pd
import matplotlib.pyplot as plt

#-----------------------------------------
#ConcreteProductB1
#-----------------------------------------

class Histograma(Graficas):
    def grafica(self) -> None:
        data = pd.read_csv('emergencias.csv')
        plt.hist(data['TITULO'])
        plt.xticks(rotation=90)
        plt.xlabel('Eventos')
        plt.ylabel('Número de evento')
        plt.title('Número de Activaciones por Evento')
        plt.show()
       