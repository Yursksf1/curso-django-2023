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
    mensaje_respuesta = '<h1> Calculo de pago  </h1> </br>'
    usuarios = suscriptore.objects.all()
    for usuario in usuarios:
        Vlor_sin=0
        total_horas_trabajadas=0
        print(usuario)
        horas_trabajadas=usuario.horas_entrenamiento_set.all()
        print( horas_trabajadas)
        for ht in horas_trabajadas:
            print(ht)
            horas_trabajadas=total_horas_trabajadas + ht.total_horas 
            t_hor_trabaja=horas_trabajadas
           # print(t_hor_trabajas)
        #mensaje_respuesta = "{} Mi nombre es {}, llevo entrenado {} horas, el valor es mi factura es {}</br>".format(mensaje_respuesta, usuario.nombre,total_horas_trabajadas,Valor_horas)           
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
        mensaje_respuesta = "{} Tu nombre es {}, llevas entrenado {} horas, el valor de tu factura es {} y el descuento por cliente {} es de {}</br>".format(mensaje_respuesta, usuario.nombre,t_hor_trabaja,Vlor_des,Tipo,Des)
    

        
                
    return HttpResponse(mensaje_respuesta)