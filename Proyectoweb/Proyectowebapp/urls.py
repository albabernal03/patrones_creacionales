from django.urls import path
from Proyectowebapp import views


urlpatterns = [
    path("", views.home, name="home"),
    path("pedir/", views.pedir, name="pedir"),
    path("ver_csv/", views.ver_csv, name="ver_csv"),
   

]