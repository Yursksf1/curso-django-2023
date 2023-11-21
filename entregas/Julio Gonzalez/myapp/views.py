from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from myapp.models import Usuarios


def index(request):
    mensaje = 'Titulo'
    for i in range(10):
        if i % 2 != 0:
            mensaje = "{} </br> {} ".format(mensaje, i)

    return HttpResponse(mensaje)

def home(request):
    mensaje_respuesta = '<h1> Bienvenido al curso de django 2023 </h1> </br>'
    usuarios = Usuarios.objects.all()
    for usuario in usuarios:
        total_horas_trabajadas = 0
        horas_trabajadas = usuario.horastrabajadas_set.all()
        for ht in horas_trabajadas:
            total_horas_trabajadas = total_horas_trabajadas + ht.total_horas

        mensaje_respuesta = "{} nombre: {}, edad: {}, horasT: {}</br>".format(
                mensaje_respuesta, 
                usuario.nombre, 
                usuario.edad, 
                total_horas_trabajadas)

    return HttpResponse(mensaje_respuesta)


''' ACTIVIDAD:
- Crear una vista con la informacion de los modelos haciendo uso del modelo de usuarios.
visualizar un listado de usuarios que muestre, el nombre, la edad, el peso, la altura y el IMC 

'''
def calcular_imc(altura, peso):
    if altura == 0:
        return 0
    altura = altura/100
    imc = peso/(altura**2)
    return round(imc, 2)


def imc(request):
    mensaje_respuesta = '<h1> Solucion Ejercicio IMC </h1> </br>'
    usuarios = Usuarios.objects.all()
    for usuario in usuarios:
        mensaje_respuesta = "{} nombre: {}, edad: {}, altura: {},  peso: {},  IMC: {}, </br>".format(
                mensaje_respuesta, 
                usuario.nombre, 
                usuario.edad, 
                usuario.altura,
                usuario.peso,
                calcular_imc(usuario.altura, usuario.peso)
            )

    return HttpResponse(mensaje_respuesta)


'''- ACTIVIDAD:
crear una nueva vista que permita calcular el total de pago que se le debe dar a cada usuario, para cada usuario.	

'''

def calcular_ht(valor, horas):
    if valor == 0:
        return 0
    if horas == 0:
        return 0
    total = valor * horas
    return round(total, 2)

def completo(nombres, apellidos):
    nombreCompleto = nombres + " " + apellidos
    return (nombreCompleto)

def htxusuario(request):
    mensaje_respuesta = '<h1> Solucion Ejercicio IMC </h1> </br>'
    usuarios = Usuarios.objects.all()
    for usuario in usuarios:
        total_horas_trabajadas = 0
        horas_trabajadas = usuario.horastrabajadas_set.all()
        for ht in horas_trabajadas:
            total_horas_trabajadas = total_horas_trabajadas + ht.total_horas
            
        mensaje_respuesta = "{} Nombre : {}, Edad : {}, Valor Hora : {}, Horas Trabajadas : {}, Total : {}</br>".format(
                mensaje_respuesta, 
                completo(usuario.nombre, usuario.apellido),
                usuario.edad,
                usuario.valorHora,
                total_horas_trabajadas,
                calcular_ht(usuario.valorHora, total_horas_trabajadas)
            )

    return HttpResponse(mensaje_respuesta)