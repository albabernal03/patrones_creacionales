from estudio import Estudio
from graficas import Graficas
from grafica_pastel import GraficaPastel
from grafica_barras import GraficaBarras

#ConcreteFactory2

class CrearGrafica(Estudio):

    def crear_calculos(self) -> CalculosEstadisticos:
        return None


    def crear_graficas(self) -> Graficas:
        return [GraficaPastel(), GraficaBarras()]

        
