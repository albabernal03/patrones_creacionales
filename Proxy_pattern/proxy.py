from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def tamaño(self):
        pass

class Documento(Component):
    def __init__(self, nombre, tipo, tamaño):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__tamaño = tamaño

    def tamaño(self):
        return self.__size
      