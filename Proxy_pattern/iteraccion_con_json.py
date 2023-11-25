from component import Component
from archivo import Archivo
from carpeta import Carpeta
from enlace import Enlace
import json

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