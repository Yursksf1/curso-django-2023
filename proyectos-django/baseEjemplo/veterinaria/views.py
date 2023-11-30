from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
# Create your views here.

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
