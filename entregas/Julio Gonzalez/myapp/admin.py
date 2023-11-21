from django.contrib import admin
from myapp.models import Usuarios, HorasTrabajadas
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','apellido','edad','altura','peso']
    
admin.site.register(Usuarios, UsuarioAdmin)
admin.site.register(HorasTrabajadas)