"""Crea un programa en Python donde podamos almacenar informacion del usuarios List(diccionario). 
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
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1 Agregar más usuarios', agregar),
        '2': ('Opción 2 Listar usuario', lista),
        '3': ('Opción 3 Calcular el promedio de [edades, peso, alturas]', promedio),
        '4': ('Opción 4 Calcular el IMC de cada usuario', imc),
        '0': ('Salir', salir)
    }

    generar_menu(opciones, '0')


def agregar():
    print('Has elegido agregar mas usuarios')


def lista():
    print('Has elegido lista de usuarios')


def promedio():
    print('Has elegido Calcular el promedio de [edades, peso, alturas]')

def imc():
    print('Has elegido Calcular el IMC de cada usuario')

def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()