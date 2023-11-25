from component import Component

#------------------------------------------------------------
#Leaf
#------------------------------------------------------------

class Enlace(Component):
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.url = destino

    def tamaño(self):
        return 0
    
