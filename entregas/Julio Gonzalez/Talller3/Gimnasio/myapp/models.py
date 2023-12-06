from django.db import models

# Create your models here.
class Suscriptor(models.Model):
    identificacion = models.PositiveIntegerField()
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.PositiveIntegerField()
    altura = models.DecimalField(max_digits=5, decimal_places=2, default=165.0)
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=80.0)
    tipoclasificacion = models.CharField(max_length=10)
    horas = models.PositiveIntegerField(default=0)
    
class Clasificacion(models.Model):
    tipoId = models.CharField(max_length=10)
    nrohoras = models.CharField(max_length=10)
    valorhoras = models.PositiveIntegerField()
    
class Horas_utilizada(models.Model):
    usuario = models.ForeignKey(Suscriptor, on_delete=models.CASCADE)
    total_horas = models.PositiveIntegerField()
    dia = models.DateField()


    # def __str__(self) -> str:
    #     return "Nombre {} horas {} Dia {} ".format(self.usuario.nombre, self.total_horas, self.dia)