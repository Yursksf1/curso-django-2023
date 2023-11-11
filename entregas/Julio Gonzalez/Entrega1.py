# Crea un programa en Python donde podamos Calcular promedios de la siguientes lista de numeros: 
# [ 1,2,3,4,4,5,6,7,8,4,3,2,4,4,4,5,6,7,2]
# X = (x1+x2+x3+x4+....+xn) / N

print('* Crea un programa en Python donde podamos Calcular promedios de la siguientes lista de numeros: ')
print('[1,2,3,4,4,5,6,7,8,4,3,2,4,4,4,5,6,7,2]')

myList = [1,2,3,4,4,5,6,7,8,4,3,2,4,4,4,5,6,7,2]
print('')
print('Lista de numeros')

sum = 0
promedio = 0
for i in myList:
    print('Numero : ', i)
    sum = sum + i
    
print('')
print('------ Resultado ------')
print('')
print ('Suma de numeros : ',sum)

n = len(myList)
print ('Cantidad de numeros : ',n)

promedio = sum / n
print('Promedio : ',promedio)
print('')
