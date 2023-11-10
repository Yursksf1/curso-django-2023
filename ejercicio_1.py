print('hola mundo')

if True:
    print('es verdad')
else:
    print('no es verdad')


for i in range(10):
    print('esto es un ciclo, estoy iterando i cuyo valor es: ', i)

bandera = True
while (bandera): 
    print('estoy dentro de un while')
    respuesta = input('ingresa 0 para salir: ')
    if respuesta == '0':
        bandera = False

# Ejercicio, 
"""
Crear un programa en python, que solicite el nombre del usuario, e imprima un saludo.
en caso que el usuario ingrese el valor 0, entonce el programa dejara de ejecutarse 
si, no, entonces seguira pidiendo nombres para saludar 
"""
