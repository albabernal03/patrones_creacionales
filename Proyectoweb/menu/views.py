from django.db import transaction
from django.shortcuts import render, redirect
from menu.models import Combo
import pandas as pd
import csv
from django.http import HttpResponse

# Create your views here.
@transaction.atomic
def menu(request):
    combos = Combo.objects.all()
    return render(request, 'menu/menu.html', {'combos':combos})

def ver_csv(request):
    csv_file_name = 'pedido.csv'  # Nombre de tu archivo CSV
    df = pd.read_csv(csv_file_name)

    # Convertir el DataFrame de pandas a una tabla HTML
    table_html = df.to_html(classes='table table-striped')

    return render(request, 'Proyectowebapp/ver_csv.html', {'table_html': table_html})



def guardar_pedido_en_csv(request):
    # Obtener el carrito de la sesión
    carro = request.session.get('carro', {})


    # Verificar si hay elementos en el carrito
    if not carro:
        return HttpResponse("El carrito está vacío.")

    # Nombre del archivo CSV
    csv_file_name = 'pedido.csv'

    # Abrir el archivo CSV en modo escritura
    with open(csv_file_name, 'w', newline='') as csvfile:
        # Definir los encabezados del CSV
        fieldnames = ['Combo ID', 'Nombre', 'Precio']

        # Crear el objeto escritor CSV
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escribir los encabezados al archivo
        writer.writeheader()

        # Escribir cada elemento del carrito al archivo
        for item in carro:
            writer.writerow({
                'Combo ID': item['id'],
                'Nombre': item['nombre'],
                'Precio': item['precio']
                # Agregar más campos según sea necesario
            })

    return HttpResponse(f"Carrito guardado exitosamente en {csv_file_name}.")



