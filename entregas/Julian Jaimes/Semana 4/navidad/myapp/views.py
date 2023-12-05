from django.shortcuts import render

# Create your views here.

from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)

from myapp.models import Usuario
from myapp.models import Cancion
from myapp.models import Receta
from myapp.models import Regalo

def Regalos(request):
    usuarios = Usuario.objects.all()
    rega = Regalo.objects.all()
    mensaje="Lista de Regalos"
    context = {
    "mensaje": mensaje,
    "mi_list": usuarios,
    "regal":rega,
    }
    return render(request, 'myapp/regalos.html', context)

def Canciones(request):
    rega = Cancion.objects.all()
    context = {
    "rega": rega,
    }
    return render(request, 'myapp/musica.html', context)

def Cocina(request):
    rega = Receta.objects.all()
    mensaje = "RECETAS"
    context = {
    "rega": rega,
    "mensaje": mensaje,

    }
    return render(request, 'myapp/recetas.html', context)

def My_Navidad(request):
    #usuarios = Usuario.objects.all()
    mensaje = "BIENVENIDOS"
    
    context = {
    "mensaje": mensaje,
    }
    return render(request, 'myapp/regalos.html', context)
    