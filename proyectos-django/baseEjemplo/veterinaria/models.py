from django.db import models

class Propietario(models.Model):
    nombre = models.CharField(max_length=200)
    celular_cli = models.PositiveIntegerField(null=True)
    email_cli = models.EmailField(max_length=200)
    fecha_nacimiento_cli = models.DateField(default=None, null=True)

    def __str__(self) -> str:
        return self.nombre

class Mascota(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    fecha_nacimiento_mas = models.DateField(default=None, null=True)
    especie_mas = models.CharField(max_length=200)
    peso_mas = models.DecimalField(max_digits=5, decimal_places=2, default=20)

    def __str__(self) -> str:
        return self.nombre
    