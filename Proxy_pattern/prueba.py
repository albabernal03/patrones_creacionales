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
        proxy_archivo1.log_access = lambda: None  # Disable log access to prevent timestamp mismatches

        acceder(proxy_archivo1, usuario_valido)

        self.assertTrue(proxy_archivo1._access_granted)
        self.assertTrue(any("Se ha accedido" in log_entry for log_entry in proxy_archivo1._access_log))

    def test_acceso_denegado(self):
        proxy_archivo1 = ComponentProxy(archivo1, access_control=['Usuario1', 'Usuario2'])
        usuario_invalido = 'UsuarioInvalido'
        proxy_archivo1.check_access = lambda: False  # Simula un acceso denegado
        proxy_archivo1.log_access = lambda: None  # Disable log access to prevent unexpected log entries

        acceder(proxy_archivo1, usuario_invalido)

        self.assertFalse(proxy_archivo1._access_granted)
        self.assertTrue(any(f"Proxy: {usuario_invalido} no tiene acceso." in log_entry for log_entry in proxy_archivo1._access_log))

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
        self.assertTrue(any(expected_log_entry in log_entry for log_entry in proxy_archivo1._access_log))


if __name__ == '__main__':
    unittest.main()