from menu import ComponentMenu
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




