# operaciones aritmeticas

print(1 + 2)
print(1 - 2)


print(3 * 4)
print(12 / 2)


print(2 ** 5)
# print(36 ** (1/2))

print('-----------')
print('0' * 10)


print('3' * 4)
print([4] * 4)

print('holaa' + 'a')

print(sum([1,2,3,4]))

# Estructuras de datos....
## listas [,,]
### help(list)
my_lista = [0,1,2,3,4]
print(my_lista)
for i in my_lista:
    print('iterando la lista: ', i)

my_lista.append(5)
my_lista.append(6)
my_lista.append(7)
print(my_lista)
print() 

my_list = [ 1,2,2,2,1,1,2,3]
my_list.count(1)
len(my_list)
my_list[5]
my_list[1]
# diccionarios
## diccionarios {key: value}

my_diccionary = {
    "nombre": "Yurley",
    "edad": 30,
    "color_favorito": "Azul"
}

my_diccionary.get("nombre")
my_diccionary['nueva_llave'] = "nuevo valor"

for key, value in my_diccionary.items():
    print("{}: {}".format(key, value))


## tuplas ()s


## Ejercicios
"""
Crear un programa en python, que solicite el nombre del usuario, e imprima un saludo.
en caso que el usuario ingrese el valor 0, entonce el programa dejara de ejecutarse 
si, no, entonces seguira pidiendo nombres para saludar

al finalizar el programa se deben ejecutar las siguientes operaciones: 
- quiero saber a cuantas personas he saludado
- quiero que se imprima un guion (-) o un asterisco (*) por cada persona que he saludado pero con un nuevo mensaje despidiendose 
    1) Juan
        - adios Juan hasta pronto! ...
    2) Mateo
        -- adios Mateo ...
    3) Camilo
        --- adios Camilo ...

- quiero que se imprima un guion (-) o un asterisco (*) por cada persona que he saludado pero con un nuevo mensaje despidiendose si es un numero par o impar
    1) Juan
        - adios Juan hasta pronto! ...
    2) Mateo
        ** adios Mateo ...
    3) Camilo
        --- adios Camilo ...
    4) David
        **** adios David ...

"""
