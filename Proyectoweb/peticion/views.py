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
@login_required(login_url='/autenticacion/login')
def procesar_peticion(request):
    peticion = Peticion.objects.create(user=request.user)
    carro = Carro(request)
    linea_peticion = []

    for key, value in carro.carro.items():
        linea_peticion.append(LineaPeticion(
            combo_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            peticion=peticion
        ))

        linea_peticion.save()  
        linea_peticion.append(linea_peticion)
    peticion.save()

    LineaPeticion.objects.bulk_create(linea_peticion)

    enviar_email(
        peticion=peticion, 
        linea_peticion=linea_peticion,
        nombreusuario=request.user.username, 
        email_usuario=request.user.email
    )

    messages.success(request, 'Pedido procesado exitosamente') 
    return redirect('../menu')     

def enviar_email(**kwargs):
    asunto = 'Pedido Procesado'
    mensaje = render_to_string('peticion/email.html', {
        'pedido': kwargs.get('peticion'),
        'lineas_pedido': kwargs.get('lineas_peticion'),
        'nombreusuario': kwargs.get('nombreusuario'),
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = 'pizzeriadelizioso@gmail.com'
    to = [kwargs.get('email_usuario')]

    send_mail(asunto, mensaje_texto, from_email, to, html_message=mensaje)
