from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myapp.models import suscriptore, Horas_entrenamiento

class UsuarioAdmin(admin.ModelAdmin):
                
    list_display = ['id', 'nombre', 'edad', 'altura','peso','ciudad', 'barrio', 'dirección']

admin.site.register(suscriptore, UsuarioAdmin)
admin.site.register(Horas_entrenamiento)