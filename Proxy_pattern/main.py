from component import Component
from carpeta import Carpeta
from archivo import Archivo
from enlace import Enlace
from proxy import ComponentProxy
from iteraccion_con_json import *
import json

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
                elemento_a_eliminar = encontrar_elemento_por_nombre(structure, nombre_elemento)

                if elemento_a_eliminar:
                    eliminar(structure, elemento_a_eliminar)
                    print(f"Elemento {nombre_elemento} eliminado.")
                    navegar(structure)
                else:
                    print(f"No se encontró el elemento {nombre_elemento}.")

            elif accion == 'nada':
                print("No se realizarán cambios.")

            else:
                print("Acción no reconocida. No se realizarán cambios.")

        else:
            print("Error loading structure from JSON.")
    else:
        print(f"{usuario}, no tienes acceso a esta estructura.")
