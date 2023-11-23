from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from peticion.models import Peticion, LineaPeticion
from carro.carro import Carro
from django.contrib import messages
from django.shortcuts import redirect
from django.db import transaction
from django.template.loader import render_to_string 
from django.utils.html import strip_tags
from django.core.mail import send_mail

@login_required(login_url='/autenticacion/login')
@transaction.atomic
def procesar_peticion(request):
    try:
        # Paso 1: Crear y guardar la instancia de Peticion
        peticion = Peticion.objects.create(user=request.user)

        # Paso 2: Crear instancias de LineaPeticion y agregarlas a la lista
        carro = Carro(request)
        lineas_peticion = []

        for key, value in carro.carro.items():
            linea_peticion = LineaPeticion(
                combo_id=key,
                cantidad=value['cantidad'],
                user=request.user,
                peticion=peticion
            )
            lineas_peticion.append(linea_peticion)

        # Paso 3: Usar bulk_create para insertar todas las instancias de LineaPeticion
        LineaPeticion.objects.bulk_create(lineas_peticion)

        # Paso 4: Guardar la instancia de Peticion después de crear las LineaPeticion
        peticion.save()

        # Paso 5: Enviar correo electrónico
        enviar_email(
            peticion=peticion, 
            lineas_peticion=lineas_peticion,
            nombreusuario=request.user.username, 
            email_usuario=request.user.email
        )

        # Paso 6: Mensaje de éxito y redirección
        messages.success(request, 'Pedido procesado exitosamente') 
        return redirect('../menu')

    except Exception as e:
        # Manejo de errores y re-lanzamiento para depuración
        print(f"Error en procesar_peticion: {e}")
        raise

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
