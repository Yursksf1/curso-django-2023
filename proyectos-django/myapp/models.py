from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.nombre
