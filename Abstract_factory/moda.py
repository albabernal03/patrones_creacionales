from calculosestadisticos import CalculosEstadisticos
import pandas as pd
from statistics import mode
#-----------------------------------------
#ConcreteProductA2
#-----------------------------------------

class Moda(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        activaciones_por_dia = datos.groupby(datos['FECHA']).size()
        return (f'La moda es: {mode(activaciones_por_dia)}')
