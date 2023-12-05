from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre_usu = models.CharField(max_length=200)
    email_usu = models.EmailField(max_length=200)
    celular_usu = models.PositiveIntegerField()
    fechanacimiento_usu = models.DateField(default=None, null=True)
    
    def __str__(self) -> str:
        return "{}".format(self.nombre_usu)
    

class regalo(models.Model):
    usuario_reg = models.ForeignKey(usuario, on_delete=models.CASCADE)
    nombre_reg = models.CharField(max_length=200)
    descripcion_reg = models.CharField(max_length=200)
    url_reg = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return " {} {} {} ".format(self.usuario_reg.nombre_usu, self.descripcion_reg, self.url_reg)
    
class cancion(models.Model):
    nombre_can = models.CharField(max_length=200)
    descripcion_can = models.CharField(max_length=200)
    url_can = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return "{}".format(self.nombre_can)
    
class receta(models.Model):
    nombre_rec = models.CharField(max_length=200)
    categoria_rec = models.CharField(max_length=200)
    descripcion_rec = models.CharField(max_length=200)
    url_rec = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return "{}".format(self.nombre_rec)
    
class pelicula(models.Model):
    nombre_pel = models.CharField(max_length=200)
    descripcion_pel = models.CharField(max_length=200)
    url_pel = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return "{}".format(self.nombre_pel)