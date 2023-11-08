from django.shortcuts import render, HttpResponse

# Create your views here. Aqui se crean las vistas de la app, en este caso de la pizzeria

def home(request):
    return render(request, "Proyectowebapp/home.html")

def pedir(request):
    return render(request, "Proyectowebapp/pedir.html")

