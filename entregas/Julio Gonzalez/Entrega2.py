"""Crea un programa en Python donde podamos calcular el IMC de un adulto
IMC             CLASIFICACION
< 18.5          Bajo Peso
18.5 - 24.9     Normal
25.0 - 29.9     Sobre peso
30.0 - 34.9     Obesidad 1
35.0 - 39.9     Obesidad 2
40.0 - 49.9     Obesidad 3
> 50            Obesidad 4
"""
print('Crea un programa en Python donde podamos calcular el IMC de un adulto')
print('')

print('--- Tabla de IMC ---')
print('IMC             CLASIFICACION')
print('< 18.5          Bajo Peso')
print('18.5 - 24.9     Normal')
print('25.0 - 29.9     Sobre peso')
print('30.0 - 34.9     Obesidad 1')
print('35.0 - 39.9     Obesidad 2')
print('40.0 - 49.9     Obesidad 3')
print('> 50            Obesidad 4')
print('')

print('---- Digite los datos ----')
print('')
peso = float(input('Cual es su peso (Kg) : '))
estatura = float(input('Cual es su estatuta : '))

print('')
print('---- Resultado ----')
imc = peso / estatura**2

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
