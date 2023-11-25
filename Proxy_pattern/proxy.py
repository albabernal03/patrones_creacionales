from abc import ABC, abstractmethod
from datetime import datetime
import json

#------------------------------------------------------------
# Component
#------------------------------------------------------------

class Component(ABC):
    @abstractmethod
    def tamaño(self):
        pass

#------------------------------------------------------------
#Leaf
#------------------------------------------------------------

class Archivo(Component):
    def __init__(self, nombre, tipo, tamaño):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__tamaño = tamaño

    def tamaño(self):
        return self.__size
      
#------------------------------------------------------------
# Composite
#------------------------------------------------------------

class Carpeta(Component):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__elementos = []

    def tamaño(self):
        total = 0
        for elemento in self.__elementos:
            total += elemento.tamaño()
        return total

    def agregar(self, elemento):
        self.__elementos.append(elemento)

    def eliminar(self, elemento):
        self.__elementos.remove(elemento)


#------------------------------------------------------------
#Leaf
#------------------------------------------------------------

class Enlace(Component):
    def __init__(self, nombre, destino):
        self.__nombre = nombre
        self.__url = destino

    def tamaño(self):
        return 0
    


#------------------------------------------------------------
# Proxy
#------------------------------------------------------------

class ComponentProxy(Component):
    def __init__(self, real_component, access_control=[]):
        self._real_component = real_component
        self._access_control = access_control
        self._access_granted = False
        self._access_log = []

    def tamaño(self):
        if self.check_access():
            return self._real_component.tamaño()
        else:
            return 0

    def check_access(self) -> bool:
        user = input("Introduce el usuario: ")
        if user in self._access_control:
            print(f"Proxy: {user} ha accedido.")
            self._access_granted = True
        else:
            print(f"Proxy: {user} no tiene acceso.")
        return self._access_granted

    def log_access(self) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"Se ha accedido: {timestamp}"
        print(f"Proxy: {log_entry}")
        self._access_log.append(log_entry)

#Funciones para interactuar con la estructura y el Proxy
def navegar(component):
    print(f"El tamaño de {component._real_component._nombre} es: {component.tamaño()}")

def agregar(carpeta, elemento):
    carpeta.agregar(elemento)

def modificar_contenido(elemento,nuevo_contenido):
    if isinstance(elemento,Archivo):
        elemento._contenido=nuevo_contenido
    else:
        print("No se puede modificar el contenido de una carpeta")

def eliminar(carpeta, elemento):
    carpeta.eliminar(elemento)

def acceder(proxy, usuario):
    proxy.check_access()
    navegar(proxy)  

def revocar_acceso(proxy, usuario):
    proxy._access_granted = False


# Función para cargar la estructura desde un archivo JSON
def cargar_estructura_desde_json(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return crear_estructura_desde_json(datos)

# Función para crear la estructura desde un diccionario
def crear_estructura_desde_json(datos):
    carpeta_raiz = crear_componente_desde_json(datos)
    return carpeta_raiz

# Función recursiva para crear un componente desde un diccionario
def crear_componente_desde_json(datos):
    tipo_componente = datos.get('tipo')
    if tipo_componente == 'Archivo':
        return Archivo(datos['nombre'], datos['tipo'], datos['tamaño'])
    elif tipo_componente == 'Carpeta':
        carpeta = Carpeta(datos['nombre'])
        for datos_hijo in datos['elementos']:
            componente_hijo = crear_componente_desde_json(datos_hijo)
            carpeta.agregar_elemento(componente_hijo)
        return carpeta
    elif tipo_componente == 'Enlace':
        return Enlace(datos['nombre'], datos['url'])

archivo1 = Archivo("Archivo1", "txt", 10)
archivo2 = Archivo("Archivo2", "pdf", 20)
carpeta1 = Carpeta("Carpeta1")
carpeta1.agregar(archivo1)
carpeta1.agregar(archivo2)
proxy_archivo1 = ComponentProxy(archivo1, access_control=['Usuario1', 'Usuario2'])
if __name__ == "__main__":
    # Cargar la estructura desde un archivo JSON
    structure = cargar_estructura_desde_json('structure.json')

    if structure:
        # Crear Proxy para el archivo
        proxy_archivo1 = ComponentProxy(archivo1, access_control=['Usuario1', 'Usuario2'])

        # Interactuar con la estructura y el Proxy
        navegar(structure)
        acceder(proxy_archivo1, "Usuario1")
        modificar_contenido(proxy_archivo1, 15)
        revocar_acceso(proxy_archivo1, "Usuario1")

        # Mostrar el estado final de la estructura
        print("\nFinal Structure:")
        navegar(structure)
    else:
        print("Error loading structure from JSON.")
