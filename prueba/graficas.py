from abc import ABC, abstractmethod

#AbstractProductB

class Graficas(ABC):
    @abstractmethod
    def grafica(self) -> None:
        pass