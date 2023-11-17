from django.contrib import admin
from myapp.models import Usuario, HorasTrabajada
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'edad', 'altura']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(HorasTrabajada)
