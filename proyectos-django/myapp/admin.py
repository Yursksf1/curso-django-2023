from django.contrib import admin
from myapp.models import Usuarios
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'edad', 'altura']

admin.site.register(Usuarios, UsuarioAdmin)