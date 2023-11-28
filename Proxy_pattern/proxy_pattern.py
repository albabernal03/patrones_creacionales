from abc import ABC, abstractmethod
from datetime import datetime
import json
import csv

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
    def __init__(self, nombre, tipo, tamano):
        self.nombre = nombre
        self.tipo = tipo
        self.tamano = tamano

    def tamaño(self):
        return self.tamano
      
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

    def eliminar(self, nombre_elemento):
        elemento_a_eliminar = encontrar_elemento_por_nombre(self, nombre_elemento)

        if elemento_a_eliminar:
            self.elementos.remove(elemento_a_eliminar)
            return elemento_a_eliminar
        else:
            return None


#------------------------------------------------------------
#Leaf
#------------------------------------------------------------

class Enlace(Component):
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.url = destino

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

    def log_access(self, usuario) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"Se ha accedido: {timestamp} por {usuario}"
        print(f"Proxy: {log_entry}")
        self._access_log.append(log_entry)
        
        # Guardar el log de acceso en un archivo CSV
        with open('access_log.csv', 'a', newline='') as csvfile:
            fieldnames = ['Timestamp', 'User']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Escribir la entrada del log en el archivo CSV
            writer.writerow({'Timestamp': timestamp, 'User': usuario})

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

def eliminar(carpeta, nombre_elemento):
    elemento_a_eliminar = encontrar_elemento_por_nombre(carpeta, nombre_elemento)

    if elemento_a_eliminar:
        carpeta.eliminar(elemento_a_eliminar)
        print(f"Elemento {nombre_elemento} eliminado.")
    else:
        print(f"No se encontró el elemento {nombre_elemento}.")

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



# Función para cargar la estructura desde un archivo JSON
def cargar_estructura_desde_json(ruta_archivo):
    print("Attempting to load data from:", ruta_archivo)
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)
        print("Loaded data from JSON:", datos)
        return crear_estructura_desde_json(datos)
    except FileNotFoundError:
        print("File not found:", ruta_archivo)
        return None
    except json.JSONDecodeError as je:
        print("JSON decoding error:", je)
        return None
    except Exception as e:
        print("Error loading data from JSON:", e)
        return None


# Función para crear la estructura desde un diccionario
def crear_estructura_desde_json(datos):
    tipo_componente = datos.get('type')

    if tipo_componente == 'Carpeta':
        carpeta = Carpeta(datos['nombre'])
        for datos_hijo in datos['elementos']:
            componente_hijo = crear_estructura_desde_json(datos_hijo)
            carpeta.agregar(componente_hijo)
        return carpeta

    elif tipo_componente == 'Archivo':
        return Archivo(datos['nombre'], datos['tipo'], datos['tamaño'])

    elif tipo_componente == 'Enlace':
        return Enlace(datos['nombre'], datos['url'])

    else:
        raise ValueError(f"Unknown component type: {tipo_componente}")


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

if __name__ == "__main__":
    # Solicitar al usuario que ingrese su nombre
    usuario = input("Introduce tu nombre de usuario: ")

    # Crear Proxy para el archivo
    proxy_archivo1 = ComponentProxy(archivo1, access_control=['Usuario1', 'Usuario2'])

    # Verificar el acceso del usuario
    if usuario in proxy_archivo1._access_control:
        print(f"Bienvenido, {usuario}.")

        # Cargar la estructura desde un archivo JSON
        structure = cargar_estructura_desde_json('structure.json')

        if structure:
    # Interactuar con la estructura y el Proxy
            navegar(structure)

            # Solicitar al usuario que elija una acción
            accion = input("¿Qué acción deseas realizar? (agregar/modificar/eliminar/nada): ")

            if accion == 'agregar':
                # Solicitar detalles para agregar un nuevo elemento
                tipo_elemento = input("Tipo de elemento (Archivo/Carpeta/Enlace): ")
                nombre_elemento = input("Nombre del elemento: ")

                if tipo_elemento == 'Archivo':
                    tamano_elemento = int(input("Tamaño del archivo: "))
                    nuevo_elemento = Archivo(nombre_elemento, 'tipo_desconocido', tamano_elemento)
                elif tipo_elemento == 'Carpeta':
                    nuevo_elemento = Carpeta(nombre_elemento)
                elif tipo_elemento == 'Enlace':
                    url_elemento = input("URL del enlace: ")
                    nuevo_elemento = Enlace(nombre_elemento, url_elemento)
                else:
                    print("Tipo de elemento desconocido. No se puede agregar.")
                    nuevo_elemento = None

                if nuevo_elemento:
                    agregar(structure, nuevo_elemento)
                    print(f"Elemento {nombre_elemento} agregado.")
                    navegar(structure)

            elif accion == 'modificar':
                # Solicitar detalles para modificar un elemento
                nombre_elemento = input("Nombre del elemento a modificar: ")
                nuevo_tamano = int(input("Nuevo tamaño: "))
                elemento_a_modificar = encontrar_elemento_por_nombre(structure, nombre_elemento)

                if elemento_a_modificar:
                    modificar_tamano(elemento_a_modificar, nuevo_tamano)
                    print(f"Tamaño de {nombre_elemento} modificado.")
                    navegar(structure)
                else:
                    print(f"No se encontró el elemento {nombre_elemento}.")

            elif accion == 'eliminar':
                # Solicitar detalles para eliminar un elemento
                nombre_elemento = input("Nombre del elemento a eliminar: ")
                eliminar(structure, nombre_elemento)
                navegar(structure)

            elif accion == 'nada':
                print("No se realizarán cambios.")
                
            else:
                print("Acción no reconocida. No se realizarán cambios.")
             # Log de acceso al archivo CSV
            proxy_archivo1.log_access(usuario)
        else:
            print("Error loading structure from JSON.")
