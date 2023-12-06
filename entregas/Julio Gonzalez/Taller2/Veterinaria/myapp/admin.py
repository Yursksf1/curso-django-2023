from django.contrib import admin
from myapp.models import Cliente, Mascota

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_cli','celular_cli','email_cli','fecha_nacimiento_cli']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Mascota)


