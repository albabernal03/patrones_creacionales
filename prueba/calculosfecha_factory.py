from analisis1_factory import Analisisdatos
from calculos_estadisticos1 import CalculosEstadisticos
from media1 import Media


#ConcreteFactory1

class Calculos_estadistico_fecha(Analisisdatos):
    def crear_calculos(self) -> CalculosEstadisticos:
        return Media()

    def crear_graficas(self) -> None:
        return None
