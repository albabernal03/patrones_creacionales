from analisis_factory import Analisisdatos
from calculos_estadisticos import CalculosEstadisticos
from media1 import Mediafecha
from moda1 import Modafecha


#ConcreteFactory1

class Calculos_estadistico_fecha(Analisisdatos):
    def crear_calculos(self) -> CalculosEstadisticos:
        return CalculosEstadisticos()

    def crear_graficas(self) -> None:
        return None
