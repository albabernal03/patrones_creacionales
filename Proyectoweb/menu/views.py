from django.db import transaction

from django.shortcuts import render, redirect
from menu.models import Combo, Componente

# Create your views here.
@transaction.atomic
def menu(request):
    combos = Combo.objects.all()
    return render(request, 'menu/menu.html', {'combos':combos})

