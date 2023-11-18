from django.shortcuts import render
from menu.models import Combo

# Create your views here.
def menu(request):
    combos = Combo.objects.all()
    return render(request, 'menu/menu.html', {'combos':combos})