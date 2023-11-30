from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)

from myapp.models import Suscriptor, Clasificacion, Horas_utilizada

# Create your views here.


def index(request):
    Tabla=''
    mensaje_respuesta = '<h2> Tipos de planes </h1> </br>'
    clasififcaciones = Clasificacion.objects.all()
    for cl in clasififcaciones:
        mensaje_respuesta = "{}, {}, {}, {}</br>".format(mensaje_respuesta, cl.tipoId, cl.nrohoras, cl.valorhoras )
        
        Tabla=''' {}<tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        </tr>
        '''.format(Tabla, cl.tipoId, cl.nrohoras, cl.valorhoras )
    mensaje_respuesta='''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <div class="container mt-3">
        <h1>*** GIMNASIO SALUD VIDA ***</h1>
        <br>
        <br>
        <h3>El ejercicio te ayuda a mejorar tu salud física y mental y a contar con un sistema inmune fuerte. Llena tu vida de energía y motivación. Supera tus límites con programas de entrenamiento diseñados por profesionales de la salud, de acuerdo con tus objetivos.</h3>
        <br>
        <h2><p>Tipos de planes</p></h2>
        <table class="table table-striped table-hover">
        <thead>
            <tr>
                <th>PLAN</th>
                <th>DIAS</th>
                <th>VALOR HORA</th>
            </tr>
        </thead>
        <tbody>
        {}
        </tbody>
        </table>
        </div>
    </body>
    </html>

    '''.format(Tabla)
    return HttpResponse(mensaje_respuesta)


def suscriptores(request):
    Tabla=''
    mensaje_respuesta = '<h2> Suscriptores  </h1> </br>'
    usuarios = Suscriptor.objects.all()
    for usuario in usuarios:
        # mensaje_respuesta = mensaje_respuesta.format(usuario.identificacion, usuario.nombre, usuario.apellido, usuario.horas)
        mensaje_respuesta = "{}, {}, {}, {}, {}, {}</br>".format(mensaje_respuesta, usuario.identificacion, usuario.nombre, usuario.apellido, usuario.altura, usuario.peso,)
        
        Tabla=''' {}<tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        </tr>
        '''.format(Tabla, usuario.identificacion, usuario.nombre, usuario.apellido, usuario.altura, usuario.peso,)
    mensaje_respuesta='''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <div class="container mt-3">
        <h1>*** GIMNASIO SALUD VIDA ***</h1>
        <h2><p>Suscriptores</p></h2>
        <table class="table">
        <thead>
            <tr>
                <th>IDENTIFICACION</th>
                <th>NOMBRE</th>
                <th>APELLIDO</th>
                <th>ALTURA</th>
                <th>PESO</th>
            </tr>
        </thead>
        <tbody>
        {}
        </tbody>
        </table>
        </div>
    </body>
    </html>

    '''.format(Tabla)
    return HttpResponse(mensaje_respuesta)


def facturar(request):
    Tabla=''
    mensaje_respuesta = '<h1> Valor a pagar por el plan  </h1> </br>'
    usuarios = Suscriptor.objects.all()
    for usuario in usuarios:
        Vlor_sin=0
        total_horas_trabajadas=0
        t_hor_trabaja=0
        horas_trabajadas=usuario.horas_utilizada_set.all()
        for ht in horas_trabajadas:
            print(ht)
            total_horas_trabajadas = total_horas_trabajadas + ht.total_horas 
            t_hor_trabaja=total_horas_trabajadas
        print(total_horas_trabajadas)
        Vlor_sin=5000*t_hor_trabaja
        if t_hor_trabaja<=15:
            print("menor 15")
            Vlor_des=5000*t_hor_trabaja
            Des=Vlor_sin-Vlor_des
            Tipo='Bronce'
        elif t_hor_trabaja>=15 and t_hor_trabaja<=30:
            print("entre 15 y 30") 
            Vlor_des=3500*t_hor_trabaja
            Des=Vlor_sin-Vlor_des
            Tipo='Plata'
        else:
            print("Mayor 30")
            Vlor_des=2000*t_hor_trabaja
            Des=Vlor_sin-Vlor_des
            Tipo='Oro'
        # mensaje_respuesta = "{} Tu nombre es {}, llevas entrenado {} horas, el valor de tu factura es {} y el descuento por cliente {} es de {}</br>".format(mensaje_respuesta, usuario.nombre,t_hor_trabaja,Vlor_des,Tipo,Des)
        Tabla=''' {}<tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        </tr>
        '''.format(Tabla, usuario.nombre,t_hor_trabaja,Vlor_des,Tipo,Des)
    mensaje_respuesta='''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <div class="container mt-3">
        <h1>*** GIMNASIO SALUD VIDA ***</h1>
        <h2><p>Detalle de los pagos</p></h2>       
        <table class="table">
        <thead>
            <tr>
            <th>Nombre</th>
            <th>Numero de Horas</th>
            <th>valor total</th>
            <th>Tipo suscripción</th>
            <th>Descuento</th>
            </tr>
        </thead>
        <tbody>
        {}
        </tbody>
        </table>
        </div>
    </body>
    </html>

    '''.format(Tabla)
    return HttpResponse(mensaje_respuesta)