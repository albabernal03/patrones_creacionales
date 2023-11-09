from calculosestadisticos import CalculosEstadisticos
import pandas as pd
from numpy import mean

#-----------------------------------------
#ConcreteProductA1
#-----------------------------------------
class Media(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        activaciones_por_dia = datos.groupby(datos['FECHA']).size()
        return (f'La media es: {activaciones_por_dia.mean()}')