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
    mensaje='''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap 5 Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<div class="container-fluid p-5 bg-primary text-white text-center">
  <h1>My First Bootstrap Page</h1>
  <p>Resize this responsive page to see the effect!</p> 
</div>
  
<div class="container mt-5">
  <div class="row">
    <div class="col-sm-4">
      <h3>{}</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
    <div class="col-sm-4">
      <h3>{}</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
    <div class="col-sm-4">
      <h3>{}</h3>        
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
  </div>
</div>

</body>
</html>'''.format(cant_user,t_hora,Prom)
    
    return HttpResponse(mensaje)
 
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
<h2>Ejemplo</h2>
<p>Resumen horas:</p>          
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


def indexx(request):
    Tabla2=''
    horas_trabajada=0
    t_hor_trabaja=0
    aa=""
    #mensaje_respuesta = '<h1> Bienvenido al curso de django 2023 </h1> </br>'
    usuarios = suscriptore.objects.all()
    for usuario in usuarios:

        Imc= float(usuario.peso/(usuario.altura*usuario.altura)*100)
        #mensaje_respuesta = "{} Mi nombre es {} tengo {} años, mido {} y peso {}, El resulatado de IMC es {}</br>".format(mensaje_respuesta, usuario.nombre, usuario.edad, usuario.altura, usuario.peso,Imc)
        
        total_horas_trabajadas=0
        horas_trabajadas=usuario.horas_entrenamiento_set.all()
        for ht in horas_trabajadas:
            total_horas_trabajadas=total_horas_trabajadas + ht.total_horas 
               
            context = {
                "a": usuario.nombre,
                "b": usuario.altura,
                "c": usuario.peso,
                "d": Imc,
                "e": total_horas_trabajadas,

                 }
    return render(request, 'myapp/indexx.html', context)