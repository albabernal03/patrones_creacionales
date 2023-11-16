from django.shortcuts import render
from .models import Combo # hemos importado el modelo Combo para poder usarlo en la vista menu

# Create your views here.
def menu(request):
    combos = Combo.objects.all()
    print(combos)
    return render(request, 'menu/menu.html', {'combos':combos})