import csv

#-----------------------------------------
#Creamos un CSV donde almacenar las elecciones de los clientes
#-----------------------------------------

from django.contrib.auth import get_user_model

user=get_user_model()


#-----------------------------------------
#Creamos un CSV donde almacenar las elecciones de los clientes
#-----------------------------------------

class PedidoCSV:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = f'Proyectoweb/Proyectowebapp/{self.file_name}'

    def write_pedido_to_csv(self, pedido):
        with open(self.file_name, mode='a', newline='') as file:
            fieldnames = ['Usuario', 'Combo', 'Cantidad', 'Precio']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            #Si el archivo está vacío o no existe, escribe la fila de encabezado
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({
                'Usuario': pedido.user,
                'Combo': pedido.combo,
                'Cantidad': pedido.cantidad,
                'Precio': pedido.precio
            })

            

