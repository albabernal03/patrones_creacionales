from menu import ComponentMenu

#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Postre(ComponentMenu):
    
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio
    
        def mostrar(self):
            print(f'Postre: {self.nombre} - Precio: {self.precio}')
