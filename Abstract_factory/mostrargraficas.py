from calculosestadisticos import CalculosEstadisticos
from graficas import Graficas
from analisisdatos_factory import Analisisdatos
from barras import GraficaBarras
from histograma import Histograma

#-----------------------------------------
#ConcreteFactory2
#-----------------------------------------

class Mostrargraficas(Analisisdatos):
    def crear_calculos(self) -> CalculosEstadisticos:
        return None

    def crear_graficas(self) -> Graficas:
        return [GraficaBarras(), Histograma()]

