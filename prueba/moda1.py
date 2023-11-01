from calculos_estadisticos import CalculosEstadisticos
from numpy import mean
import pandas as pd

#concreteProductA2

class Modafecha(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        datos['FECHA'] = pd.to_datetime(datos['FECHA'], errors='coerce')
        activaciones_por_dia = datos.groupby(datos['FECHA'].dt.date).size()
        return activaciones_por_dia.mode()