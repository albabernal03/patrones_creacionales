from estudio import Estudio
from calculosestadisticos import CalculosEstadisticos
from media import Media
from moda import Moda
from mediana import Mediana
from graficas import Graficas
#ConcreteFactory1

class Calculos_estadistico(Estudio):
    def crear_calculos(self) -> CalculosEstadisticos:
        return [Media(), Moda(), Mediana()]


    def crear_graficas(self) -> Graficas:
        return None