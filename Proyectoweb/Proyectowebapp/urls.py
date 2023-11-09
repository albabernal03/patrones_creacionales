from django.urls import path
from Proyectowebapp import views


urlpatterns = [
    path("", views.home, name="home"),
    path("pedir/", views.pedir, name="pedir"),
    path("ver_csv/", views.ver_csv, name="ver_csv"),
    path('revisar_pedido/', views.revisar_pedido, name='revisar_pedido'),
    path('confirmar_modificar_pedido/', views.confirmar_modificar_pedido, name='confirmar_modificar_pedido'),
    path('modificar_pedido/', views.modificar_pedido, name='modificar_pedido'),

]