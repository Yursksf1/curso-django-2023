from django.db import models

# Create your models here.
class Propietario(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre
    

# Create your models here.
class Mascota(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre
    