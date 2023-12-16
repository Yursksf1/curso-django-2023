from django.shortcuts import render, redirect

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

def Cocina_receta(request, id_receta):
    rega = Receta.objects.filter(id = id_receta).first()
    mensaje = "RECETAS - Detalle"
    context = {
        "rega": None,
        "mensaje": mensaje,
    }
    if rega:
        context["rega"] = rega

    return render(request, 'myapp/recetas_detail.html', context)

def Cocina_create(request):
    mensaje = "RECETAS - crear"

    if request.method == 'POST':
        data_receta  = request.POST
        # definir los atributos del nuevo registro
        receta = data_receta.get('receta')
        decripcion = data_receta.get('decripcion')
        puntuacion = data_receta.get('puntuacion')

        # crear el registro 
        rc = Receta()
        rc.receta = receta
        rc.decripcion = decripcion
        rc.puntuacion = puntuacion
        rc.save()

        return redirect("app:cocina")

    context = {
        "rega": None,
        "mensaje": mensaje,
    }

    return render(request, 'myapp/recetas_create.html', context)

def Cocina_import(request):
    mensaje = "RECETAS - Import"

    if request.method == 'POST':
        receta_import_file = request.FILES["receta_import_file"]
        # TODO: Agregar validacion sobre el archivo: ej: https://pythoncircle.com/post/30/how-to-upload-and-process-the-csv-file-in-django/

        file_data = receta_import_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            records_values = line.split(',')
            receta = records_values[0]
            decripcion = records_values[1]

            rc = Receta()
            rc.receta = receta
            rc.decripcion = decripcion
            rc.save()


        return redirect("app:cocina")

    context = {
        "rega": None,
        "mensaje": mensaje,
    }

    return render(request, 'myapp/recetas_import.html', context)

def My_Navidad(request):
    #usuarios = Usuario.objects.all()
    mensaje = "BIENVENIDOS"
    
    context = {
    "mensaje": mensaje,
    }
    return render(request, 'myapp/regalos.html', context)
    