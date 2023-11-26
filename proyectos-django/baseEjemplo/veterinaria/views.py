from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
# Create your views here.

def index(request):
    messsage = "Hola mundo aca vamos a renderizar los registros de los propietarios"


    # Your code is here
    '''
    nombre de los propietarios en un texto
    '''

    return HttpResponse(messsage)