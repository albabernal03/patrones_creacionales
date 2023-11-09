from django.shortcuts import render, HttpResponse, redirect
from .form import PizzaBuilderForm
from .models import Pizza
from .storage import PizzaCSV
import csv
import pandas as pd

# Create your views here. Aqui se crean las vistas de la app, en este caso de la pizzeria

def home(request):
    return render(request, "Proyectowebapp/home.html")

def pedir(request):
    masa = ""  # Provide default values or empty strings for variables
    salsa = ""
    ingredientes_principales = ""
    coccion = ""
    presentacion = ""
    maridaje_recomendado = ""
    extra = ""

    if request.method == 'POST':
        form = PizzaBuilderForm(request.POST)
        if form.is_valid():
            masa=form.cleaned_data['masa']
            salsa=form.cleaned_data['salsa']
            ingredientes_principales=form.cleaned_data['ingredientes_principales']
            coccion=form.cleaned_data['coccion']
            presentacion=form.cleaned_data['presentacion']
            maridaje_recomendado=form.cleaned_data['maridaje_recomendado']
            extra=form.cleaned_data['extra_bordes_queso']

        pizza_order= Pizza(
            masa=masa,
            salsa=salsa,
            ingredientes_principales=ingredientes_principales,
            coccion=coccion,
            presentacion=presentacion,
            maridaje_recomendado=maridaje_recomendado,
            extra=extra
        )
        pizza_order.save()
        # Guarda los datos en un archivo CSV
        csv_file_name = 'pizza.csv'
        pizza_csv = PizzaCSV(csv_file_name)
        pizza_csv.write_pizza_to_csv(pizza_order)
        return render(request,'Proyectowebapp/home.html')
      
    
    else:
        form = PizzaBuilderForm()

    return render(request, "Proyectowebapp/pedir.html", {'form': form})



def ver_csv(request):
    csv_file_name = 'pizza.csv'  # Nombre de tu archivo CSV
    df = pd.read_csv(csv_file_name)

    # Convertir el DataFrame de pandas a una tabla HTML
    table_html = df.to_html(classes='table table-striped')

    return render(request, 'Proyectowebapp/ver_csv.html', {'table_html': table_html})


def resumen_pedido(request):
    if request.method == 'POST':
        form= PizzaBuilderForm(request.POST)
        if form.is_valid():
            masa=form.cleaned_data['masa']
            salsa=form.cleaned_data['salsa']
            ingredientes_principales=form.cleaned_data['ingredientes_principales']
            coccion=form.cleaned_data['coccion']
            presentacion=form.cleaned_data['presentacion']
            maridaje_recomendado=form.cleaned_data['maridaje_recomendado']
            extra=form.cleaned_data['extra_bordes_queso']

            return render(request, 'Proyectowebapp/resumen_pedido.html', {'masa': masa, 'salsa': salsa, 'ingredientes_principales': ingredientes_principales, 'coccion': coccion, 'presentacion': presentacion, 'maridaje_recomendado': maridaje_recomendado, 'extra': extra, 'form': form})
        
    return redirect ('pedir')





def confirmar_modificar_pedido(request):
    if request.method == 'POST':
        decision = request.POST.get('decision')

        if decision == 'confirmar':
            # Obtener los datos del resumen_pedido
            masa = request.POST.get('masa')
            salsa = request.POST.get('salsa')
            ingredientes_principales = request.POST.get('ingredientes_principales')
            coccion = request.POST.get('coccion')
            presentacion = request.POST.get('presentacion')
            maridaje_recomendado = request.POST.get('maridaje_recomendado')
            extra = request.POST.get('extra_bordes_queso')

            # Guardar los datos en un archivo CSV
            csv_file_name = 'pizza.csv'
            with open(csv_file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Masa', 'Salsa', 'Ingredientes Principales', 'Cocción', 'Presentación', 'Maridaje Recomendado', 'Extra'])
                writer.writerow([masa, salsa, ingredientes_principales, coccion, presentacion, maridaje_recomendado, extra])

            return render(request, 'Proyectowebapp/ver_csv.html', {'masa': masa, 'salsa': salsa, 'ingredientes_principales': ingredientes_principales, 'coccion': coccion, 'presentacion': presentacion, 'maridaje_recomendado': maridaje_recomendado, 'extra': extra})
        
        elif decision == 'modificar':
            return redirect('pedir')

    return HttpResponse("Invalid decision or appropriate response")
