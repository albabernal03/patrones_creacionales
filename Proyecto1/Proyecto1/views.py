from django.http import HttpResponse

#creamos una primera vista
def saludo(request):
    return HttpResponse("Hola mundo desde Django")