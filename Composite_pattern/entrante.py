from menu import ComponentMenu
#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Entrante(ComponentMenu):
        
            def __init__(self, nombre, precio):
                self.nombre = nombre
                self.precio = precio
        
            def mostrar(self):
                print(f'Entrante: {self.nombre} - Precio: {self.precio}')


