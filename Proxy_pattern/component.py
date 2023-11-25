from abc import ABC, abstractmethod

#------------------------------------------------------------
# Component
#------------------------------------------------------------

class Component(ABC):
    @abstractmethod
    def tamaño(self):
        pass

