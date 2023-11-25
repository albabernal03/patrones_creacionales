from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pedido, LineaPedido
from carro.carro import Carro
from django.contrib import messages
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items():
        lineas_pedido.append(LineaPedido(user=request.user,combo_id=key,pedido=pedido,cantidad=value['cantidad']))

    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )

    messages.success(request,f'Pedido N°{pedido.id} creado exitosamente')
    return redirect('home')


def enviar_mail(**kwargs):
    asunto='Gracias por tu pedido'
    mensaje=render_to_string('emails/pedido.html',{
        'pedido':kwargs.get('pedido'),
        'lineas_pedido':kwargs.get('lineas_pedido'),
        'nombreusuario':kwargs.get('nombreusuario')
    })

    mensaje_texto=strip_tags(mensaje)
    from_email='pizzeriadelizioso@gmail.com'
    #to_email=kwargs.get('emailusuario')
    to_email='albabr08@gmail.com'

    send_mail(asunto,mensaje_texto,from_email,[to_email],html_message=mensaje)


  