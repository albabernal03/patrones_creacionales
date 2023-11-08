from django.http import HttpResponse
import datetime

def saludo(request): # primera vista
    documento= '''
    <html>
        <body>
            <h1>Hola Mundo</h1>
        </body>


'''
    return HttpResponse(documento)

def fecha(request): 
    fecha_actual=datetime.datetime.now()
    documento= '''
    <html>
        <body>
            <h1>Fecha y hora actuales %s</h1>
        </body>

    

''' % fecha_actual
    
    return HttpResponse(documento)
