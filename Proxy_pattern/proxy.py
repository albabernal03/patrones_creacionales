from abc import ABC, abstractmethod
from datetime import datetime

#------------------------------------------------------------
# Component
#------------------------------------------------------------

class Component(ABC):
    @abstractmethod
    def tamaño(self):
        pass

#------------------------------------------------------------
#Leaf
#------------------------------------------------------------

class Archivo(Component):
    def __init__(self, nombre, tipo, tamaño):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__tamaño = tamaño

    def tamaño(self):
        return self.__size
      
#------------------------------------------------------------
# Composite
#------------------------------------------------------------

class Carpeta(Component):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__elementos = []

    def tamaño(self):
        total = 0
        for elemento in self.__elementos:
            total += elemento.tamaño()
        return total

    def agregar(self, elemento):
        self.__elementos.append(elemento)

    def eliminar(self, elemento):
        self.__elementos.remove(elemento)


#------------------------------------------------------------
#Leaf
#------------------------------------------------------------

class Enlace(Component):
    def __init__(self, nombre, destino):
        self.__nombre = nombre
        self.__url = destino

    def tamaño(self):
        return 0
    


#------------------------------------------------------------
# Proxy
#------------------------------------------------------------

class ComponentProxy(Component):
    def __init__(self, real_component, access_control=[]):
        self._real_component = real_component
        self._access_control = access_control
        self._access_granted = False
        self._access_log = []

    def tamaño(self):
        if self.check_access():
            return self._real_component.tamaño()
        else:
            return 0

    def check_access(self) -> bool:
        user = input("Introduce el usuario: ")
        if user in self._access_control:
            print(f"Proxy: {user} ha accedido.")
            self._access_granted = True
        else:
            print(f"Proxy: {user} no tiene acceso.")
        return self._access_granted

    def log_access(self) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"Se ha accedido: {timestamp}"
        print(f"Proxy: {log_entry}")
        self._access_log.append(log_entry)

        