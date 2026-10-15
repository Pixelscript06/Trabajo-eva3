from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('objetos', views.objetos, name='objetos'),
    path('objetos/crear', views.crear, name='crear'),
    path('objetos/detalle/<int:id>', views.detalle, name='detalle'),
    path('objetos/editar/<int:id>', views.editar, name='editar'),
    path('objetos/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('api/objetos/', views.objeto_list),
    path('api/objetos/<int:pk>', views.objeto_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
