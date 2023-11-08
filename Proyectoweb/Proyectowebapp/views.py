from django.shortcuts import render, HttpResponse

# Create your views here. Aqui se crean las vistas de la app, en este caso de la pizzeria

def home(request):
    return HttpResponse('Home')

def pedir(request):
    return HttpResponse('Pedir')

