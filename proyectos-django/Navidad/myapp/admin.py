from django.contrib import admin

# Register your models here.

from django.contrib import admin
from myapp.models import Usuario,Regalo,Cancion,Receta

class UsuarioAdmin(admin.ModelAdmin):
                
    list_display = ['id', 'nombre', 'correo', 'celular','año_nacimiento']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Regalo)
admin.site.register(Cancion)
admin.site.register(Receta)