from django.shortcuts import render

# Create your views here.

from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.contrib.auth.decorators import login_required
from myapp.models import Usuario
from myapp.models import Cancion
from myapp.models import Receta
from myapp.models import Regalo


@login_required
def index(request):
    messsage_base = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1> Programa de veterinaria 0.1 </h1>
            <h2> 
                Propietarios
            </h2>
            <p>
            {}
            </p>
            <h2> 
                Mascotas
            </h2>
            <p>
            {}
            </p>
            
        </body>
        </html>
    """
    usuarios = ["Yurley", "Juan"]
    mascotas = ["Manchitas", "patitas", "micho"]
    
    messsage = messsage_base.format(
        usuarios, mascotas
    )
    # Your code is here
    '''
    nombre de los propietarios en un texto
    '''
    return HttpResponse(messsage)


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
    