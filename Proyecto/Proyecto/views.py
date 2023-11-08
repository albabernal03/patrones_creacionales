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
            <h2>Fecha y hora actuales %s</h2>
        </body>

    

''' % fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request, agno):
    edadActual=18
    periodo=agno-2021
    edadFutura=edadActual+periodo
    documento= '''
    <html>
        <body>
            <h2>En el año %s tendras %s años</h2>
        </body>

    

''' %(agno, edadFutura)
    
    return HttpResponse(documento)