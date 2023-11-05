from abc import ABC, abstractmethod
import pandas as pd 
from numpy import mean
from numpy import median
from scipy import stats #libreria para calcular moda
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode


#-----------------------------------------
#AbstractProductA
#-----------------------------------------

class CalculosEstadisticos(ABC):
    @abstractmethod
    def calcular(self) -> float:
        pass


#-----------------------------------------
#AbstractProductB
#-----------------------------------------

class Graficas(ABC):
    @abstractmethod
    def grafica(self) -> None:
        pass


#-----------------------------------------
#AbstractFactory
#-----------------------------------------

class Analisisdatos(ABC):
    @abstractmethod
    def crear_calculos(self) -> CalculosEstadisticos:
        pass

    @abstractmethod
    def crear_graficas(self) -> Graficas:
        pass

#-----------------------------------------
#ConcreteProductA1
#-----------------------------------------

class Media(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        datos['FECHA'] = pd.to_datetime(datos['FECHA'], errors='coerce')
        activaciones_por_dia = datos.groupby(datos['FECHA'].dt.date).size()
        return (f'La media es: {activaciones_por_dia.mean()}')

#-----------------------------------------
#ConcreteProductA2
#-----------------------------------------

class Moda(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        datos['FECHA'] = pd.to_datetime(datos['FECHA'], errors='coerce')
        activaciones_por_dia = datos.groupby(datos['FECHA'].dt.date).size()
        return (f'La moda es: {mode(activaciones_por_dia)}')


#-----------------------------------------
#ConcreteProductA3
#-----------------------------------------

class Mediana(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        datos['FECHA'] = pd.to_datetime(datos['FECHA'], errors='coerce')
        activaciones_por_dia = datos.groupby(datos['FECHA'].dt.date).size()
        return (f'La mediana es: {activaciones_por_dia.median()}')

    
#-----------------------------------------
#ConcreteProductB1
#-----------------------------------------

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
       

#-----------------------------------------
#ConcreteProductB2
#-----------------------------------------

class Histograma(Graficas):
    def grafica(self) -> None:
        data = pd.read_csv('emergencias.csv')
        data['ID-EVENTO'] = pd.to_datetime(data['FECHA'], errors='coerce')
        # Agrupar por fecha y contar las activaciones por día
        activaciones_por_dia = data.groupby(data['FECHA'].dt.date).size()
        # Visualizar el número de activaciones por día
        activaciones_por_dia.plot(kind='hist', figsize=(10, 6))
        plt.xlabel('Fecha')
        plt.ylabel('Número de Activaciones')
        plt.title('Número de Activaciones por Día')
        plt.show()
     


#-----------------------------------------
#ConcreteFactory1
#-----------------------------------------

class Calculosmmm(Analisisdatos):
    def crear_calculos(self) -> CalculosEstadisticos:
        return [Media(), Mediana(), Moda()]

    def crear_graficas(self) -> Graficas:
        return None


#-----------------------------------------
#ConcreteFactory2
#-----------------------------------------

class Mostrargraficas(Analisisdatos):
    def crear_calculos(self) -> CalculosEstadisticos:
        return None

    def crear_graficas(self) -> Graficas:
        return [GraficaBarras(), Histograma()]


#-----------------------------------------
#Client
#-----------------------------------------


def main():
    factory=Calculosmmm()

    calculos=factory.crear_calculos()

    for i in calculos:
        print(i.calcular())

    factory=Mostrargraficas()

    mostrar=factory.crear_graficas()

    for i in mostrar:
        i.grafica()


if __name__ == "__main__":
    main()
   
'''
# Client
def main():
    factory=Mostrargraficas()

    mostrar=factory.crear_graficas()

    for i in mostrar:
        i.grafica()

    

if __name__ == "__main__":
    main()
'''
