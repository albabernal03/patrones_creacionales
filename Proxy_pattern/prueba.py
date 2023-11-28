from main import *
import unittest
import unittest

class TestEstructura(unittest.TestCase):

    def test_proxy_access_granted(self):
        # Crear Proxy con acceso concedido a un usuario
        proxy_archivo = ComponentProxy(Archivo("Archivo1", "txt", 10), access_control=['Usuario1'])

        # Verificar que el acceso se concede para el usuario especificado
        self.assertTrue(proxy_archivo.check_access())

    def test_proxy_access_denied(self):
        # Crear Proxy con acceso denegado a un usuario
        proxy_archivo = ComponentProxy(Archivo("Archivo1", "txt", 10), access_control=['Usuario2'])

        # Verificar que el acceso se deniega para el usuario especificado
        self.assertFalse(proxy_archivo.check_access())

    def test_modificar_tamano_archivo(self):
        # Crear un archivo
        archivo = Archivo("Archivo1", "txt", 10)

        # Modificar el tamaño del archivo
        modificar_tamano(archivo, 20)

        # Verificar que el tamaño del archivo se ha modificado correctamente
        self.assertEqual(archivo.tamano, 20)

    def test_agregar_elemento_a_carpeta(self):
        # Crear una carpeta
        carpeta = Carpeta("Carpeta1")

        # Crear un archivo para agregar a la carpeta
        archivo = Archivo("Archivo1", "txt", 10)

        # Agregar el archivo a la carpeta
        agregar(carpeta, archivo)

        # Verificar que el archivo se ha agregado a la carpeta
        self.assertIn(archivo, carpeta.elementos)

    def test_eliminar_elemento_de_carpeta(self):
        # Crear una carpeta
        carpeta = Carpeta("Carpeta1")

        # Crear un archivo y agregarlo a la carpeta
        archivo = Archivo("Archivo1", "txt", 10)
        agregar(carpeta, archivo)

        # Eliminar el archivo de la carpeta
        eliminar(carpeta, archivo)

        # Verificar que el archivo se ha eliminado de la carpeta
        self.assertNotIn(archivo, carpeta.elementos)

# Agregar más tests según sea necesario...

if __name__ == "__main__":
    unittest.main()
