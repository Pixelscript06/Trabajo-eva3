from django.contrib import admin
from .models import ObjetoPerdido

# Register your models here.
class ObjetoPerdidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'categoria', 'lugar_hallazgo', 'fecha_hallazgo', 'estado']

admin.site.register(ObjetoPerdido, ObjetoPerdidoAdmin)
