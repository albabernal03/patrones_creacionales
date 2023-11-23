from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from peticion.models import Peticion, LineaPeticion
from carro.carro import Carro
from django.contrib import messages
from django.shortcuts import redirect
from django.template.loader import render_to_string 
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url='/autenticacion/logear')
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

    enviar_email(
        peticion= peticion, 
        lineas_peticion=lineas_peticion,
        nombre_usuario=requets.user.username, 
        email_usuario=requets.user.email
        )

    messages.success(requets, 'Pedido procesado exitosamente') 
    return redirect('../menu')     

def enviar_email(**kwargs):
    asunto= 'Pedido Procesado'
    mensaje= render_to_string('peticion/email.html',{
        'pedido': kwargs.get['peticion'],
        'lineas_pedido': kwargs.get['lineas_peticion'],
        'nombreusuario': kwargs.get['nombreusuario'],

    })

    mensaje_texto=strip_tags(mensaje)
    from_email='pizzeriadelizioso@gmail.com'
    #to=[kwargs.get['email_usuario']]
    to='albabr08@gmail.com'

    send_mail(asunto, mensaje_texto, from_email,[to], html_message=mensaje)
