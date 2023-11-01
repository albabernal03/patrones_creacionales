from analisis_factory import Analisisdatos
from calculos_estadisticos1 import CalculosEstadisticos
from media1 import Mediafecha


#ConcreteFactory1

class Calculos_estadistico_fecha(Analisisdatos):
    def crear_calculos(self) -> CalculosEstadisticos:
        return Mediafecha()

    def crear_graficas(self) -> None:
        return None
