from django.db import models
from abc import ABC, abstractmethod

# Create your models here.

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

#-----------------------------------------
#Concrete Builder
#-----------------------------------------

class Pizza():
    def __init__(self,masa,salsa,ingredientes_principales,coccion,presentacion,maridaje_recomendado,extra):
        self.masa= masa
        self.salsa= salsa
        self.ingredientes_principales= ingredientes_principales
        self.coccion= coccion
        self.presentacion= presentacion
        self.maridaje_recomendado= maridaje_recomendado
        self.extra= extra