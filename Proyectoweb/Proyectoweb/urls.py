"""
URL configuration for Proyectoweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from menu.views import ver_pedido_csv

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('Proyectowebapp.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('menu/', include('menu.urls')),
    path('carro/', include('carro.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('ver_pedido_csv/', ver_pedido_csv, name='ver_pedido_csv'),
   
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
