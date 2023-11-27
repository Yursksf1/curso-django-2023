from django.shortcuts import render

# Create your views here.
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
# Create your views here.
from myapp.models import suscriptore


def index(request):
    mensaje = 'Titulo'
    for i in range(10):
        if i % 2 != 0:
            mensaje = "{} </br> {} ".format(mensaje, i)

    return HttpResponse(mensaje)
 
def Horas(request):
    mensaje_respuesta = '<h1> Calculo pago usurio </h1> </br>'
    usuarios = suscriptore.objects.all()
    for usuario in usuarios:
        total_horas_trabajadas=0
        horas_trabajadas=usuario.horas_entrenamiento_set.all()
        for ht in horas_trabajadas:
            total_horas_trabajadas=total_horas_trabajadas + ht.total_horas 
            Valor_horas=total_horas_trabajadas 
        mensaje_respuesta = "{} Mi nombre es {}, He trabajado {} horas extras y el valor es de $ {}</br>".format(mensaje_respuesta, usuario.nombre,total_horas_trabajadas,Valor_horas)           

    return HttpResponse(mensaje_respuesta)