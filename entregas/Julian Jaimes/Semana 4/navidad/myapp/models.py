from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200, default="")
    correo = models.EmailField(default="")
    celular = models.PositiveBigIntegerField(max_length=10, default=0000000000 )
    año_nacimiento = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.nombre
    

class Regalo(models.Model):
    nombre = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    regalo=models.CharField(max_length=50, default="")
    decripcion = models.CharField(max_length=200, default="")
    url=models.URLField(null=True, blank=True,  # <=====
        verbose_name="Dirección Web")
    
    
    
    def __str__(self) -> str:
        return "Usuario   {} regalo   {}   Descripción  {}   url".format(self.nombre, self.regalo, self.decripcion,self.url)

class Receta(models.Model):
    receta=models.CharField(max_length=50, default="")
    decripcion = models.CharField(max_length=200, default="")
    
    
    
    def __str__(self) -> str:
        return " Receta  {}  descriipción  {} ".format( self.receta, self.decripcion)

class Cancion(models.Model):
    cancion=models.CharField(max_length=50, default="")
    url = models.CharField(max_length=200, default="")
    
    
    
    def __str__(self) -> str:
        return " Cancion  {}  Url  {} ".format( self.cancion, self.url)