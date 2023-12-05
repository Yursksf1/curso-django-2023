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


def Index(request):
    t_hora=0
    cant_user=0
    mensaje = '<h1> Calculo de pago  </h1> </br>'
    usuarios = suscriptore.objects.all()
    for usuario in usuarios:
        cant_user=cant_user+1
        Vlor_sin=0
        total_horas_trabajadas=0
        print(usuario)
        horas_trabajadas=usuario.horas_entrenamiento_set.all()
        print( horas_trabajadas)
        for ht in horas_trabajadas:
            
            print(ht)
            horas_trabajadas=total_horas_trabajadas + ht.total_horas 
            t_hor_trabaja=horas_trabajadas
        t_hora=t_hora+ ht.total_horas 
    
    Prom=t_hora/cant_user
    
         
    context = {
    "cant": cant_user,
    "hora": t_hora,
    "prom": Prom,
    
    }
    return render(request, 'myapp/nuevo.html', context)
    #return HttpResponse(mensaje,'myapp/indexx.html',context)
 
def Horas(request):
    Tabla=''
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
        #mensaje_respuesta = "{} Tu nombre es {}, llevas entrenado {} horas, el valor de tu factura es {} y el descuento por cliente {} es de {}</br>".format(mensaje_respuesta, usuario.nombre,t_hor_trabaja,Vlor_des,Tipo,Des)
        
        Tabla=(Tabla, usuario.nombre,t_hor_trabaja,Vlor_des,Tipo,Des)
    print(Tabla)
    context = {
    "mi_list": Tabla,
    }
    return render(request, 'myapp/horas.html', context)
        
                
    return HttpResponse(mensaje_respuesta)

def Imc(request):
    Tabla2=''
    horas_trabajada=0
    t_hor_trabaja=0
    
    #mensaje_respuesta = '<h1> Bienvenido al curso de django 2023 </h1> </br>'
    usuarios = suscriptore.objects.all()
    for usuario in usuarios:

        Imc= float(usuario.peso/(usuario.altura*usuario.altura)*100)
        #mensaje_respuesta = "{} Mi nombre es {} tengo {} años, mido {} y peso {}, El resulatado de IMC es {}</br>".format(mensaje_respuesta, usuario.nombre, usuario.edad, usuario.altura, usuario.peso,Imc)
        
        total_horas_trabajadas=0
        horas_trabajadas=usuario.horas_entrenamiento_set.all()
        for ht in horas_trabajadas:
            print(ht)
            total_horas_trabajadas=total_horas_trabajadas + ht.total_horas 
            
        #t_hora=t_hora+ ht.total_horas 
        


        Tabla2=''' {}<tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            </tr>
            '''.format(Tabla2, usuario.nombre,usuario.edad, usuario.altura, usuario.peso,Imc,total_horas_trabajadas)
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
<h2>Ejemplo</h2>
<p>Resumen horas:</p>          
<table class="table">
  <thead>
    <tr>
      
      <th>Nombre</th>
      <th>Edad</th>
      <th>Altura</th>
      <th>Peso</th>
      <th>IMC</th>
      <th>Total horas</th>
    </tr>
  </thead>
  <tbody>
  {}
  </tbody>
</table>
</div>




</body>
</html>

'''.format(Tabla2)
    return HttpResponse(mensaje_respuesta)  


def Inicio(request):
    Tabla2=''
    horas_trabajada=0
    t_hor_trabaja=0
    mi_list=""
    new_list=""
    #mensaje_respuesta = '<h1> Bienvenido al curso de django 2023 </h1> </br>'
    usuarios = suscriptore.objects.all()
    for usuario in usuarios:

        Imc= float(usuario.peso/(usuario.altura*usuario.altura)*100)
        #mensaje_respuesta = "{} Mi nombre es {} tengo {} años, mido {} y peso {}, El resulatado de IMC es {}</br>".format(mensaje_respuesta, usuario.nombre, usuario.edad, usuario.altura, usuario.peso,Imc)
        
        total_horas_trabajadas=0
        horas_trabajadas=usuario.horas_entrenamiento_set.all()
        for ht in horas_trabajadas:
            total_horas_trabajadas=total_horas_trabajadas + ht.total_horas 


    mi_list=[usuario.nombre, usuario.edad, usuario.altura, usuario.peso,Imc]
    print(mi_list)
            #new_list.append(mi_list)
            
    print(usuarios)       
    context = {
    "mi_list": usuarios,
    }
    return render(request, 'myapp/indexx.html', context)