from analisis_factory import Analisisdatos
from graficas import Graficas
from graficabarras1 import GraficaBarras

#ConcreteFactory2

class CrearGrafica_fecha(Analisisdatos):
    
        def crear_calculos(self) -> None:
            return None
    
    
        def crear_graficas(self) -> Graficas:
            return GraficaBarras()

