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

        print("Decision:", decision)  # Debugging statement

        if decision == 'confirmar':
            print("Confirmar pedido")  # Debugging statement

            # Obtén el último pedido confirmado desde la base de datos
            last_order = Pizza.objects.latest('id')

            # Guarda los datos del último pedido en el formulario en un archivo CSV
            csv_file_name = 'pizza.csv'
            pizza_csv = PizzaCSV(csv_file_name)
            pizza_csv.write_pizza_to_csv(last_order, include_form_data=True)

            return redirect('home')
        
        elif decision == 'modificar':
            print("Modificar pedido")  # Debugging statement
            return redirect('pedir')  # Modifica esta línea para redirigir a la vista 'pedir'

    print("No decision found")  # Debugging statement
    return HttpResponse("Invalid decision or appropriate response")
