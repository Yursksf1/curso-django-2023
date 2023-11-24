from django.contrib import admin

# Register your models here.
from veterinaria.models import Propietario,  Mascota

admin.site.register(Propietario)
admin.site.register(Mascota)
