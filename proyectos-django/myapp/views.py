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

        mensaje_respuesta = "{} {}: {} </br>".format(mensaje_respuesta, usuario.nombre, usuario.edad)

    return HttpResponse(mensaje_respuesta)