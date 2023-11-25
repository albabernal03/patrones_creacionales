from component import Component
from datetime import datetime
from carpeta import Carpeta
from archivo import Archivo

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

    # Forwarding attribute access to the real component
    def __getattr__(self, attr):
        return getattr(self._real_component, attr)


#Funciones para interactuar con la estructura y el Proxy
def navegar(component):
    print(f"El tamaño de {component.nombre} es: {component.tamaño()}")

def agregar(carpeta, elemento):
    carpeta.agregar(elemento)

def modificar_tamano(archivo, nuevo_tamano):
    if isinstance(archivo, Archivo):
        archivo.tamano = nuevo_tamano
        print(f"El tamaño del archivo {archivo.nombre} ha sido modificado a {nuevo_tamano}")
    else:
        print("No se puede modificar el tamaño de una carpeta")

def eliminar(carpeta, elemento):
    carpeta.eliminar(elemento)

def acceder(proxy, usuario):
    proxy.check_access()
    navegar(proxy)  

def revocar_acceso(proxy, usuario):
    proxy._access_granted = False

def encontrar_elemento_por_nombre(component, nombre):
    # Verifica si el componente actual tiene el nombre buscado
    if hasattr(component, 'nombre') and component.nombre == nombre:
        return component

    # Si el componente es una carpeta, busca en sus elementos
    if isinstance(component, Carpeta):
        for elemento in component.elementos:
            resultado = encontrar_elemento_por_nombre(elemento, nombre)
            if resultado:
                return resultado

    # Si no se encuentra en el componente actual ni en sus elementos, retorna None
    return None

