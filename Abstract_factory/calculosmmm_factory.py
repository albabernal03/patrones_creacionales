from analisisdatos_factory import Analisisdatos
from media import Media
from moda import Moda
from mediana import Mediana
from calculosestadisticos import CalculosEstadisticos
from graficas import Graficas


#-----------------------------------------
#ConcreteFactory1
#-----------------------------------------

class Calculosmmm(Analisisdatos):
    def crear_calculos(self) -> CalculosEstadisticos:
        return [Media(), Mediana(), Moda()]

    def crear_graficas(self) -> Graficas:
        return None

