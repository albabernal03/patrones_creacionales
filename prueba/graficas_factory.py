from analisis1_factory import Analisisdatos
from graficas1 import Graficas
from graficabarras1 import Graficabarras

#ConcreteFactory2

class CrearGrafica(Analisisdatos):
    
        def crear_calculos(self) -> None:
            return None
    
    
        def crear_graficas(self) -> Graficas:
            return Graficabarras()

            