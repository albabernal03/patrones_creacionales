from calculos_estadisticos1 import CalculosEstadisticos
from numpy import mean
import pandas as pd
#concreteProductA1

class Media(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        return datos.['FECHA'].mean()