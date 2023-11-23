from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from peticion.models import Peticion, LineaPeticion
from carro.carro import Carro
from django.contrib import messages


# Create your views here.
@login_required(login_url='/autenticacion/login')
def procesar_peticion(requets):
    peticion=Peticion.objects.created(user=requets.user)
    carro=Carro(requets)
    lineas_peticion=list()
    for key, value in carro.carro.items():
        lineas_peticion.append(LineaPeticion(
            combo_id=key,
            cantidad=value['cantidad'],
            user=requets.user,
            peticion=peticion



        ))

    LineaPeticion.objects.bulk_create(lineas_peticion) #para añaadir varios objetos a la vez

    messages.success(requets, 'Pedido procesado exitosamente')      
