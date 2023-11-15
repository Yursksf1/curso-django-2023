my_lista = []

for i in range(5):
    nombre = input('ingrese nombre {}: '.format(i))    
    edad = float(input('ingrese edad {}: '.format(i)))
    my_lista.append(
        {
          "nombre": nombre,  
          "edad": edad,  
        }
    )

print('imprimendo la lista completa')
for i in my_lista:
    print(i)


print('calcular promedio de edad')
suma_edad = 0.0
for i in my_lista:
    suma_edad = suma_edad + i['edad']

print('total de edades: ', suma_edad)
print('total de registros: ', len(my_lista))
print('promedios de edades: ', suma_edad/len(my_lista))

promedio = sum([item['edad'] for item in my_lista])/len(my_lista)
print('promedios de edades v2: ', suma_edad/len(my_lista))
