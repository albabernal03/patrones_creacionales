from abc import ABC, abstractmethod


#------------------------------------------------------------
# Component
#------------------------------------------------------------

class ComponentMenu(ABC):
    '''La clase Componente base define operaciones comunes para objetos de composición,
    ya sean simples o complejos'''

    @abstractmethod
    def mostrar(self):
        pass
