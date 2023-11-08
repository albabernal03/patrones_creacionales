from django.shortcuts import render, HttpResponse
from .form import PizzaBuilderForm
from Proyectowebapp.models import Pizza

# Create your views here. Aqui se crean las vistas de la app, en este caso de la pizzeria

def home(request):
    return render(request, "Proyectowebapp/home.html")

def pedir(request):
    if request.method == 'POST':
        form = PizzaBuilderForm(request.POST)
        if form.is_valid():
            masa=form.cleaned_data['masa']
            salsa=form.cleaned_data['salsa']
            ingredientes_principales=form.cleaned_data['ingredientes_principales']
            coccion=form.cleaned_data['coccion']
            presentacion=form.cleaned_data['presentacion']
            maridaje_recomendado=form.cleaned_data['maridaje_recomendado']
            extra=form.cleaned_data['extra']

        pizza= Pizza(
            masa=masa,
            salsa=salsa,
            ingredientes_principales=ingredientes_principales,
            coccion=coccion,
            presentacion=presentacion,
            maridaje_recomendado=maridaje_recomendado,
            extra=extra
        )



    return render(request, "Proyectowebapp/pedir.html")

