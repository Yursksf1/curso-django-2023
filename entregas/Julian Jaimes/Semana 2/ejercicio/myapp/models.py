from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.PositiveIntegerField()
    altura = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    peso = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    valor_x_hora = models.PositiveIntegerField(default=30000)
    def __str__(self) -> str:
        return self.nombre
    

class HorasTrabajada(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total_horas = models.PositiveIntegerField()
    dia = models.DateField()
    
    
    def __str__(self) -> str:
        return "Nombre {} horas {} Dia {} ".format(self.usuario.nombre, self.total_horas, self.dia)

 
