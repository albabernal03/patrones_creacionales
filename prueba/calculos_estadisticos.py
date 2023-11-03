from abc import ABC, abstractmethod

#AbstractProductA

class CalculosEstadisticos(ABC):
    @abstractmethod
    def calcular(self) -> float:
        pass

    
class Media(CalculosEstadisticos):
    def calcular(self) -> float:
        pass

class Moda(CalculosEstadisticos):
    def calcular(self) -> float:
        pass