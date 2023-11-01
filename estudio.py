from abc import ABC, abstractmethod
from calculosestadisticos import CalculosEstadisticos
from graficas import Graficas

#AbstractFactory

class Estudio(ABC):
    @abstractmethod
    def crear_calculos(self) -> CalculosEstadisticos:
        pass

    @abstractmethod
    def crear_graficas(self) -> Graficas:
        pass