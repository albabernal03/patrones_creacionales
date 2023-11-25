from django.db import models
from django.contrib.auth import get_user_model
from menu.models import Combo
from django.db.models import F, FloatField, Sum

# Create your models here.
User=get_user_model()
class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    @property

    def total(self):
        return self.lineapedido_set.all().aggregate(total=Sum(F('combo_id__precio')*F('cantidad'), output_field=FloatField()))['total']
    
    class Meta:
        verbose_name="pedido"
        verbose_name_plural="pedidos"
        ordering=['id']

class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    combo_id=models.ForeignKey(Combo, on_delete=models.CASCADE)
    pedido_id=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.combo_id.nombre}'
    
    class Meta:
        db_table='lineapedidos'
        verbose_name='Línea Pedido'
        verbose_name_plural='Líneas Pedidos'
        ordering=['id']
