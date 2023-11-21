from django.db import models
from django.contrib.auth import get_user_model
from menu.models import Combo


# Create your models here.

User=get_user_model
class Peticion(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    @property
    def total(self):
        pass 


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