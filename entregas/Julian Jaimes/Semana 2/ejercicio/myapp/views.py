from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
# Create your views here.
from myapp.models import Usuario

def index(request):
    mensaje = 'Titulo'
    for i in range(10):
        if i % 2 != 0:
            mensaje = "{} </br> {} ".format(mensaje, i)

    return HttpResponse(mensaje)

def Imc(request):
    mensaje_respuesta = '<h1> Bienvenido al curso de django 2023 </h1> </br>'
    usuarios = Usuario.objects.all()
    for usuario in usuarios:

        Imc= float(usuario.peso/(usuario.altura*usuario.altura))
        mensaje_respuesta = "{} Mi nombre es {} tengo {} años, mido {} y peso {}, El resulatado de IMC es {}</br>".format(mensaje_respuesta, usuario.nombre, usuario.edad, usuario.altura, usuario.peso,Imc)

    return HttpResponse(mensaje_respuesta)  

def Horas(request):
    mensaje_respuesta = '<h1> Calculo pago usurio </h1> </br>'
    usuarios = Usuario.objects.all()
    for usuario in usuarios:
        total_horas_trabajadas=0
        horas_trabajadas=usuario.horastrabajada_set.all()
        for ht in horas_trabajadas:
            total_horas_trabajadas=total_horas_trabajadas + ht.total_horas 
            Valor_horas=total_horas_trabajadas*usuario.valor_x_hora   
            mensaje_respuesta = "{} Mi nombre es {}, He trabajado {} horas extras y el valor es de $ {}</br>".format(mensaje_respuesta, usuario.nombre,total_horas_trabajadas,Valor_horas)           

    return HttpResponse(mensaje_respuesta)