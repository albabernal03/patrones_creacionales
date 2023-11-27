from main import *
import unittest

class TestSistemaArchivos(unittest.TestCase):

    def setUp(self):
        # Configuración común para las pruebas, si es necesario.
        pass

    def tearDown(self):
        # Limpieza después de cada prueba, si es necesario.
        pass

    def test_acceso_exitoso(self):
        proxy_archivo1 = ComponentProxy(archivo1, access_control=['Usuario1', 'Usuario2'])
        usuario_valido = 'Usuario1'
        proxy_archivo1.check_access = lambda: True  # Simula un acceso exitoso

        acceder(proxy_archivo1, usuario_valido)

        self.assertTrue(proxy_archivo1._access_granted)
        self.assertIn(f"El tamaño de {archivo1.nombre} es: {archivo1.tamaño()}", proxy_archivo1._access_log)

    def test_acceso_denegado(self):
        proxy_archivo1 = ComponentProxy(archivo1, access_control=['Usuario1', 'Usuario2'])
        usuario_invalido = 'UsuarioInvalido'
        proxy_archivo1.check_access = lambda: False  # Simula un acceso denegado

        acceder(proxy_archivo1, usuario_invalido)

        self.assertFalse(proxy_archivo1._access_granted)
        self.assertIn(f"Proxy: {usuario_invalido} no tiene acceso.", proxy_archivo1._access_log)
        self.assertNotIn(f"El tamaño de {archivo1.nombre} es: {archivo1.tamaño()}", proxy_archivo1._access_log)

    def test_modificar_tamano(self):
        nuevo_tamano = 20
        archivo_modificado = Archivo("Archivo1", "txt", nuevo_tamano)

        modificar_tamano(archivo1, nuevo_tamano)

        self.assertEqual(archivo1.tamano, nuevo_tamano)

    def test_eliminar_elemento(self):
        nuevo_elemento = Archivo("NuevoArchivo", "txt", 15)
        carpeta_test = Carpeta("CarpetaTest")
        agregar(carpeta_test, nuevo_elemento)

        eliminar(carpeta_test, nuevo_elemento)

        self.assertNotIn(nuevo_elemento, carpeta_test.elementos)

    def test_registro_de_acceso(self):
        proxy_archivo1 = ComponentProxy(archivo1, access_control=['Usuario1', 'Usuario2'])
        usuario_valido = 'Usuario1'
        proxy_archivo1.check_access = lambda: True  # Simula un acceso exitoso

        acceder(proxy_archivo1, usuario_valido)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expected_log_entry = f"Proxy: Se ha accedido: {timestamp}"
        self.assertIn(expected_log_entry, proxy_archivo1._access_log)


if __name__ == '__main__':
    unittest.main()