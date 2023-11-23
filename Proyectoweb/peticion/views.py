from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from carro.carro import Carro

from peticion.models import LineaPeticion, Peticion

from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.core.mail import send_mail

from .models import Combo


# Create your views here.


@login_required(login_url='/autenticacion/logear')
def procesar_peticion(request):
    peticion=Peticion.objects.create(user=request.user) # damos de alta un pedido
    carro=Carro(request)  # cogemos el carro
    lineas_peticion=list()  # lista con los pedidos para recorrer los elementos del carro
    for key, value in carro.carro.items(): #recorremos el carro con sus items
        lineas_peticion.append(LineaPeticion(
            combo_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            peticion=peticion                
            ))

    LineaPeticion.objects.bulk_create(lineas_peticion) # crea registros en BBDD en paquete
    #enviamos mail al cliente
    enviar_mail(
        peticion=peticion,
        lineas_peticion=lineas_peticion,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
        

    )
    #mensaje para el futuro
    messages.success(request, "El pedido se ha creado correctamente")
    
    return redirect('../tienda')
    #return redirect('listado_productos')
    #return render(request, "tienda/tienda.html",{"productos":productos})
    

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "peticion": kwargs.get("peticion"),
        "lineas_peticion": kwargs.get("lineas_peticion"),
        "nombreusuario":kwargs.get("nombreusuario") 
                       
        })

    mensaje_texto=strip_tags(mensaje)
    from_email="cursos@pildorasinformaticas.es"
    #to=kwargs.get("email_usuario")
    to="pizzeriadelizioso@gmail.com"
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)
    
