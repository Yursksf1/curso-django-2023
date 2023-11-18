from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from myapp.models import Usuario


def index(request):
    mensaje = 'Titulo'
    for i in range(10):
        if i % 2 != 0:
            mensaje = "{} </br> {} ".format(mensaje, i)

    return HttpResponse(mensaje)

def home(request):
    mensaje_respuesta = '<h1> Bienvenido al curso de django 2023 </h1> </br>'
    usuarios = Usuario.objects.all()
    for usuario in usuarios:
        total_horas_trabajadas = 0
        horas_trabajadas = usuario.horastrabajada_set.all()
        for ht in horas_trabajadas:
            total_horas_trabajadas = total_horas_trabajadas + ht.total_horas

        mensaje_respuesta = "{} nombre: {}, edad: {}, horasT: {}</br>".format(mensaje_respuesta, usuario.nombre, usuario.edad, total_horas_trabajadas)

    return HttpResponse(mensaje_respuesta)


''' ACTIVIDAD:
- Crear una vista con la informacion de los modelos haciendo uso del modelo de usuarios.
visualizar un listado de usuarios que muestre, el nombre, la edad, el peso, la altura y el IMC 

'''