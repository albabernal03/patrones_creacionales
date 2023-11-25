from component import Component

#------------------------------------------------------------
# Composite
#------------------------------------------------------------

class Carpeta(Component):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def tamaño(self):
        total = 0
        for elemento in self.elementos:
            total += elemento.tamaño()
        return total

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        self.elementos.remove(elemento)
