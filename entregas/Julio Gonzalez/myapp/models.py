from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.PositiveIntegerField()
    altura = models.DecimalField(max_digits=5, decimal_places=2, default=165.0)
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=165.0)
    valorHora = models.PositiveIntegerField(default=30)
    
    def __str__(self) -> str:
        return self.nombre
    
class HorasTrabajadas(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    total_horas = models.PositiveIntegerField()
    dia = models.DateField()

def __str__(self) -> str:
    return "{} {} {}".format(self.usuarios.nombre, self.total_horas, self.dia)