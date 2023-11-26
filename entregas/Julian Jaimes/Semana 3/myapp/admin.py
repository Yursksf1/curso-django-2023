from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myapp.models import Usuario, HorasTrabajada

class UsuarioAdmin(admin.ModelAdmin):
                
    list_display = ['id', 'nombre', 'edad', 'altura','peso','valor_x_hora']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(HorasTrabajada)