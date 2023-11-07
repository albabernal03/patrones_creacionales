from calculosestadisticos import CalculosEstadisticos
import pandas as pd
from numpy import median


#-----------------------------------------
#ConcreteProductA3
#-----------------------------------------

class Mediana(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        activaciones_por_dia = datos.groupby(datos['FECHA']).size()
        return (f'La mediana es: {activaciones_por_dia.median()}')
    

