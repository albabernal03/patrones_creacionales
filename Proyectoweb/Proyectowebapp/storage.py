import csv
#-----------------------------------------
#Creamos un CSV donde almacenar las elecciones de los clientes
#-----------------------------------------

class PizzaCSV:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = f'Proyectoweb/Proyectowebapp/{self.file_name}'

    def write_pizza_to_csv(self, pizza, include_form_data=False):
        with open(self.file_name, mode='a', newline='') as file:
            fieldnames = ['Masa', 'Salsa', 'Ingredientes Principales', 'Cocción', 'Presentación', 'Maridaje', 'Extras']

            # Include 'Form Data' in fieldnames if include_form_data is True
            if include_form_data:
                fieldnames.append('Form Data')

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Si el archivo está vacío o no existe, escribe la fila de encabezado
            if file.tell() == 0:
                writer.writeheader()

            pizza_data = {
                'Masa': pizza.masa,
                'Salsa': pizza.salsa,
                'Ingredientes Principales': ', '.join(pizza.ingredientes_principales),
                'Cocción': pizza.coccion,
                'Presentación': pizza.presentacion,
                'Maridaje': pizza.maridaje_recomendado,
                'Extras': pizza.extra
            }

            # Add form data if include_form_data is True
            if include_form_data:
                pizza_data['Form Data'] = 'Value'  # Replace 'Value' with the actual form data

            writer.writerow(pizza_data)
