from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre_cli = models.CharField(max_length=200)
    celular_cli = models.PositiveIntegerField()
    email_cli = models.EmailField(max_length=200)
    fecha_nacimiento_cli = models.DateField()
     
    def __str__(self) -> str:
        return "{} {}".format(self.nombre, self.fecha_nacimiento_cli)

class Mascota(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre_mas = models.CharField(max_length=200)
    fecha_nacimiento_mas = models.DateField()
    especie_mas = models.CharField(max_length=200)
    peso_mas = models.DecimalField(max_digits=5, decimal_places=2, default=20)
    

def __str__(self) -> str:
    return "{} {} {}".format(self.cliente.nombre_cli, self.nombre_mas, self.fecha_nacimiento_mas)