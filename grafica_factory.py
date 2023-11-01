from estudio import Estudio
from graficas import Graficas
from graficapastel import GraficaPastel
from graficabarras import GraficaBarras

#ConcreteFactory2

class CrearGrafica(Estudio):

    def crear_calculos(self) -> CalculosEstadisticos:
        return None


    def crear_graficas(self) -> Graficas:
        return [GraficaPastel(), GraficaBarras()]


