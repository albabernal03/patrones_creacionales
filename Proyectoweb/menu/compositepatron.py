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


#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Bebida(ComponentMenu):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f'Bebida: {self.nombre} - Precio: {self.precio}')

#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Postre(ComponentMenu):
    
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio
    
        def mostrar(self):
            print(f'Postre: {self.nombre} - Precio: {self.precio}')

#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Entrante(ComponentMenu):
        
            def __init__(self, nombre, precio):
                self.nombre = nombre
                self.precio = precio
        
            def mostrar(self):
                print(f'Entrante: {self.nombre} - Precio: {self.precio}')



#------------------------------------------------------------
# Composite
#------------------------------------------------------------

class Combo(ComponentMenu):

    '''
    La clase Compuesto representa los componentes complejos que pueden tener hijos. Por lo general, 
    los objetos Compuesto delegan el trabajo real a sus hijos y luego "resumen" el resultado.
    '''

    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        self.elementos.remove(elemento)
    
    def mostrar(self):
        print(f'Combo: {self.nombre}')

        for elemento in self.elementos:
            elemento.mostrar()

        print(f'Precio Total del Combo: {self.calcular_precio_total()}')

    def calcular_precio_total(self):
        return sum(elemento.precio for elemento in self.elementos)


#------------------------------------------------------------
# Composite
#------------------------------------------------------------

# TODO: mejora el código para que se muestre esta parte distinta
class ComboPareja(ComponentMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.combo1 = None
        self.combo2 = None

    def personalizar(self, combo1, combo2):
        self.combo1 = combo1
        self.combo2 = combo2

    def mostrar(self):
        print(f'Combo Pareja: {self.nombre}')
        if self.combo1:
            print(f'Menu:')
            self.combo1.mostrar()
        if self.combo2:
            print(f'Menu:')
            self.combo2.mostrar()
        print(f'Precio Total del Combo Pareja: {self.calcular_precio_total()}')

    def calcular_precio_total(self):
        total_combo1 = self.combo1.calcular_precio_total() if self.combo1 else 0
        total_combo2 = self.combo2.calcular_precio_total() if self.combo2 else 0
        return total_combo1 + total_combo2