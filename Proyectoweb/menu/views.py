from django.db import transaction

from django.shortcuts import render, redirect
from menu.models import Combo, Componente

# Create your views here.
@transaction.atomic
def menu(request):
    combos = Combo.objects.all()
    return render(request, 'menu/menu.html', {'combos':combos})

from django.shortcuts import render, redirect
from .models import Combo, Componente

def personalizar_combo(request):
    if request.method == 'POST':
        # Obtén los IDs de los componentes seleccionados desde el formulario
        componente_ids = request.POST.getlist('componentes')

        # Consulta los componentes seleccionados desde la base de datos
        componentes_seleccionados = Componente.objects.filter(id__in=componente_ids)

        # Calcula el precio total sumando los precios de los componentes seleccionados
        precio_total = sum(componente.precio for componente in componentes_seleccionados)

        # Crea el combo personalizado con el precio total calculado
        combo_personalizado = Combo.objects.create(nombre='Combo Personalizado', precio=precio_total)

        # Agrega los componentes al combo personalizado
        combo_personalizado.componentes.set(componentes_seleccionados)

        # Redirige a una página de confirmación o a la página del combo personalizado
        return redirect('detalle_combo', combo_id=combo_personalizado.id)

    # Obtén todos los componentes para mostrar en el formulario
    todos_los_componentes = Componente.objects.all()

    return render(request, 'Proyectowebapp/personalizar_combo.html', {'todos_los_componentes': todos_los_componentes})
