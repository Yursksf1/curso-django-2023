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
    condicion = True
    usuarios = suscriptore.objects.all()
    variable = "I1"
    my_list = [1,2,3,4,5,'hola',7,8,9,'mundo']


    for ln in my_list:
        # your code is here 
        print(ln)

    context = {
        "variable": variable,
        "usuarios": usuarios,
        "condicion": condicion,
        "my_list": my_list,
        # "nombre2": 123
    }
    return render(request, 'myapp/index.html', context)

def tabla_1(request):
    condicion = True
    usuarios = suscriptore.objects.all()
    variable = "T1"
    my_list = [1,2,3,4,5,'hola',7,8,9,'mundo']


    for ln in my_list:
        # your code is here 
        print(ln)

    context = {
        "variable": variable,
        "usuarios": usuarios,
        "condicion": condicion,
        "my_list": my_list,
        # "nombre2": 123
    }
    return render(request, 'myapp/tabla_1.html', context)

 
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
        mensaje_respuesta = "{} Tu nombre es {}, llevas entrenado {} horas, el valor de tu factura es {} y el descuento por cliente {} es de {}</br>".format(mensaje_respuesta, usuario.nombre,t_hor_trabaja,Vlor_des,Tipo,Des)
        
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
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="javascript:void(0)">Logo</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="mynavbar">
            <ul class="navbar-nav me-auto">
              <li class="nav-item">
                <a class="nav-link" href="/">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/Horas1">Hora1</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/Horas2">Hora2</a>
              </li>
            </ul>
            <form class="d-flex">
              <input class="form-control me-2" type="text" placeholder="Search">
              <button class="btn btn-primary" type="button">Search</button>
            </form>
          </div>
        </div>
      </nav>



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