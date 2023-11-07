from abc import ABC, abstractmethod

#-----------------------------------------
#Product
#-----------------------------------------

class Pizza():
    def __init__(self):
        self.masa= ''
        self.salsa= ''
        self.ingredientes_principales= []
        self.coccion= [] 
        self.presentacion= ''
        self.maridaje_recomendado= ''
        self.extra= []

#-----------------------------------------
#Abstract Builder
#-----------------------------------------

class PizzaBuilder(ABC):

    @abstractmethod
    def añadir_masa(self):
        pass

    @abstractmethod
    def añadir_salsa(self):
        pass

    @abstractmethod
    def añadir_ingredientes_principales(self):
        pass

    @abstractmethod
    def añadir_coccion(self):
        pass

    @abstractmethod
    def añadir_presentacion(self):
        pass

    @abstractmethod
    def añadir_maridaje_recomendado(self):
        pass

    @abstractmethod
    def añadir_extra(self):
        pass

    @abstractmethod
    def get_pizza(self):
        return self.pizza
    


