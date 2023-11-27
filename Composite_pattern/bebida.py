from menu import ComponentMenu
#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Bebida(ComponentMenu):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f'Bebida: {self.nombre} - Precio: {self.precio}')