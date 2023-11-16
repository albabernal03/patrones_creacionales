# Importa la nueva estructura
from menu.models import Componente

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')

        if not carro:
            carro = self.session['carro'] = {}
        else:
            self.carro = carro

    def agregar(self, componente_id):
        componente = Componente.objects.get(id=componente_id)
        if str(componente.id) not in self.carro.keys():
            self.carro[str(componente.id)] = {
                'componente_id': componente.id,
                'nombre': componente.nombre,
                'precio': str(componente.precio),
                'cantidad': 1,
                'imagen': componente.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(componente.id):
                    value['cantidad'] = value['cantidad'] + 1
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def eliminar(self, componente_id):
        componente_id = str(componente_id)
        if componente_id in self.carro:
            del self.carro[componente_id]
            self.guardar_carro()

    def restar_producto(self, componente_id):
        componente_id = str(componente_id)
        for key, value in self.carro.items():
            if key == componente_id:
                value['cantidad'] = value['cantidad'] - 1
                if value['cantidad'] < 1:
                    self.eliminar(componente_id)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session['carro'] = {}
        self.session.modified = True
