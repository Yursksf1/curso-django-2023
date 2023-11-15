"""Crea un programa en Python donde podamos almacenar informacion de usuarios List(diccionario). 
-	nombre
-	apellido
-	edad 
-	peso 
-	altura

Presentar las siguientes opciones: 
-	Opcion 1) Agregar más usuarios
-	Opcion 2) Listar usuario
-	Opcion 3) Calcular el promedio de [edades, peso, alturas]
-	Opcion 4) Calcular el IMC de cada usuario
-	Opcion 0) Salir

"""

miDiccionario = {}
import sys;

def menu_principal():

    while True:
        print("--- Menu Principal")
        print('')
        print("1. Agregar más usuarios")
        print("2. Listar usuario")
        print("3. Calcular el promedio de [edades, peso, alturas]")
        print("4. Calcular el IMC de cada usuario")
        print("0. Salir")
        
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            adicionar()
        elif opcion == "2":
            listar()
        elif opcion == "3":
            promedio()
        elif opcion == "4":
            imc()
        elif opcion == "0":
            salir()
        else:
            print("Opción inválida. Intente nuevamente.")
            
def adicionar():
    print('')
    print('Adicionar usuarios')
    nombre = input('Ingrese el nombre del usuario: ')
    miDiccionario['nombre'] = nombre
    
    apellido = input('Ingrese el apellido del usuario: ')
    miDiccionario['apellido'] = apellido
    
    edad = float(input('Ingrese la edad del usuario: '))
    miDiccionario['edad'] = edad

    peso = float(input('Ingrese el peso del usuario: '))
    miDiccionario['peso'] = peso
    
    altura = float(input('Ingrese la altura del usuario: '))
    miDiccionario['altura'] = altura

def listar():
    print('')
    print('--- Lista de usuarios ---')
    for key, value in miDiccionario.items():
        print("{}: {}".format(key, value))
    print('')
    
def promedio():
    print('')
    print('promedio')
    
def imc():
    print('')
    print('imc')
    for key, value in miDiccionario.items():
        print("{}: {}".format(key, value))
        print('---- Resultado ----')
        pesoImc = miDiccionario.get('peso')
        alturaImc = miDiccionario.get('altura')
        imc = pesoImc / alturaImc

        print('Su IMC es : ',round(imc,2))
        datos = 'De acuerdo a la tabla, su nivel de peso es : '
        if imc < 18.5:
            print(datos,'Bajo peso')
        elif 18.5 <= imc <= 24.9:
            print(datos,'Normal')
        elif 25 <= imc <= 29.9:
            print(datos,'Sobre peso')
        elif 30 <= imc <= 34.9:
            print(datos,'Obesidad 1')
        elif 35 <= imc <= 39.9:
            print(datos,'Obesidad 2')
        elif 40 <= imc <= 49.9:
            print(datos,'Obesidad 3')
        else: 
            print(datos,'Obesidad 4')
        print('')

def salir():
    print('')
    print("¡Hasta luego!")
    sys.exit()
            
if __name__ == '__main__':
    menu_principal()
