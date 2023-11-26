from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.menu, name='menu'),
    path('guardar_pedido_en_csv/', views.guardar_pedido_en_csv, name='guardar_pedido_en_csv'),
   

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)