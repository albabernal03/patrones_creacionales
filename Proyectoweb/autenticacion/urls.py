from django.urls import path
from . import views

urlspatterns = [
    path('', views.autenticacion, name='autenticacion'),
]
