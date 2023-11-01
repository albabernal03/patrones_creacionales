from abc import ABC, abstractmethod
from calculos_estadisticos1 import CalculosEstadisticos
from graficas import Graficas

#AbstractFactory

class Analisisdatos(ABC):
    @abstractmethod
    def crear_calculos(self) -> CalculosEstadisticos:
        pass

    @abstractmethod
    def crear_graficas(self) -> Graficas:
        pass