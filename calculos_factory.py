from estudio import Estudio
from calculos_estadisticos import CalculosEstadisticos
from media import Media
from moda import Moda
from mediana import Mediana

#ConcreteFactory1

class Calculos_estadistico(Estudio):
    def crear_calculos(self) -> CalculosEstadisticos:
        return [Media(), Moda(), Mediana()]


    def crear_graficas(self) -> Graficas:
        return None