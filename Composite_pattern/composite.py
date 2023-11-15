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

#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Pizza(ComponentMenu):

    '''La clase Hoja representa los elementos finales en una composición. Una hoja no tiene elementos adicionales.
    En general, son las hojas las que realizan el trabajo real, mientras que los objetos Compuesto solo delegan 
    en sus partes internas.'''

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


    def mostrar(self):
        print(f'Pizza: {self.nombre} - Precio: {self.precio}')

        


    
