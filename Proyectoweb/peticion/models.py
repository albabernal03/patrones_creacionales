from django.db import models
from django.contrib.auth import get_user_model
from menu.models import Combo
from django.db.models import Sum, F, FloatField

# Create your models here.

User=get_user_model
class Peticion(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    @property
    def total(self):
        return self.lineapedidos_set.aggregate(total=Sum(F('combo_id__precio')*F('cantidad'), output_field=FloatField()))['total']


    class Meta:
        dt_table='peticion'
        verbose_name='peticion'
        verbose_name_plural='peticiones'
        ordering=['id']

class LineaPeticion(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    combo_id=models.ForeignKey(Combo, on_delete=models.CASCADE)
    peticio_id=models.ForeignKey(Peticion, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{self.cantidad} unidades de {self.combo_id.nombre}'
    
    class Meta:
        dt_table='lineapedidos'
        verbose_name='Línea Pedido'
        verbose_name_plural='Línea Pedidos'
        ordering=['id']
    

