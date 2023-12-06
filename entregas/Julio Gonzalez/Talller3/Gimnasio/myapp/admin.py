from django.contrib import admin
from myapp.models import Suscriptor, Clasificacion, Horas_utilizada

# Register your models here.

class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ['identificacion','nombre','apellido','edad','altura','peso','tipoclasificacion','horas']
    

class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ['tipoId','nrohoras','valorhoras']
    
class HorasAdmin(admin.ModelAdmin):
    list_display = ['usuario','total_horas','dia']
    
admin.site.register(Suscriptor, SuscriptorAdmin)
admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(Horas_utilizada, HorasAdmin)