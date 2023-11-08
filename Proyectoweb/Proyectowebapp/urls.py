from django.urls import path
from Proyectowebapp import views


urlpatterns = [
    path("", views.home, name="home"),
    path("pedir/", views.pedir, name="pedir"),
    path('home.html', views.home, name='home'),
]