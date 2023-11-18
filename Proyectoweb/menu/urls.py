from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.menu, name='menu'),
    path('personalizar_combo/', personalizar_combo, name='personalizar_combo'),
   

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)