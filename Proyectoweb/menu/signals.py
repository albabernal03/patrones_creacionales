# menu/signals.py
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Combo

@receiver(m2m_changed, sender=Combo.componentes.through)
def actualizar_precio_total(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.precio = instance.calcular_precio_total()
        instance.save()
I