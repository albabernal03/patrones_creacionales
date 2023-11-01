from abc import ABC, abstractmethod

#AbstractProductA

class CalculosEstadisticos(ABC):
    @abstractmethod
    def calcular(self) -> float:
        pass
