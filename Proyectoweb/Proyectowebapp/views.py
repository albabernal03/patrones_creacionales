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

        return render(request, "Proyectowebapp/pedido_resumen.html", {
                'masa': masa,
                'salsa': salsa,
                'ingredientes_principales': ingredientes_principales,
                'coccion': coccion,
                'presentacion': presentacion,
                'maridaje_recomendado': maridaje_recomendado,
                'extra': extra,
            })
    
    else:
        form = PizzaBuilderForm()

    return render(request, "Proyectowebapp/pedir.html", {'form': form})

def confirmar_pedido(request):
    if request.method == 'POST':
        masa = request.POST.get('masa')
        salsa = request.POST.get('salsa')
        ingredientes_principales = request.POST.get('ingredientes_principales')
        coccion = request.POST.get('coccion')
        presentacion = request.POST.get('presentacion')
        maridaje_recomendado = request.POST.get('maridaje_recomendado')
        extra = request.POST.get('extra')

        pizza_order = Pizza(
            masa=masa,
            salsa=salsa,
            ingredientes_principales=ingredientes_principales,
            coccion=coccion,
            presentacion=presentacion,
            maridaje_recomendado=maridaje_recomendado,
            extra=extra
        )
        pizza_order.save()

        # Guardar los datos en un archivo CSV (o donde prefieras)
        csv_file_name = 'pizza.csv'
        pizza_csv = PizzaCSV(csv_file_name)
        pizza_csv.write_pizza_to_csv(pizza_order)

        return HttpResponse("¡Pedido confirmado!")
    return redirect('home')

def ver_csv(request):
    csv_file_name = 'pizza.csv'
    df = pd.read_csv(csv_file_name)
    table_html = df.to_html(classes='table table-striped')
    return render(request, 'Proyectowebapp/ver_csv.html', {'table_html': table_html})