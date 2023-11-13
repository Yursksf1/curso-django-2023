import pandas as pd
llave=0
Ent=10
Ent=int(Ent)
lista=[]
while Ent!=0:
    print("\nElija un número\n")
    print("Opcion 1 Agregar más usuarios ") 
    print("Opcion 2 Listar usuario ")
    print("Opcion 3 Calcular el promedio de [edades, peso, alturas] " )
    print("Opcion 4 Calcular el IMC de cada usuario ")
    print("Opcion 0 Salir \n ")
    print('Ingrese un número')
    Sel=int(input()) 
    if Sel==1: 
        llave=1
        print('Ingresa tu nombre')
        Nom=input()
        print('Ingresa tu apellido')
        Ape=input()
        print('Ingresa tu edad')
        Eda=int(input())
        print('Ingresa tu peso')
        Pes=float(input())
        print('Ingresa tu altura')
        Alt=float(input())
        imc=Pes/(Alt*Alt)
        Temp_lista ={'Nombre':Nom, 'Apellido':Ape,'Edad': Eda, 'Peso':Pes, 'Altura': Alt, "IMC":imc}
        lista.append(Temp_lista)
        df = pd.DataFrame(lista)
        print(lista)
    elif Sel==2:
        if llave==1:
            print(df)
        else:
            print("Sin informacion para mostrar")  
    elif Sel==3:
        if llave==1:
            print('El promedio de edad es: {}'. format(df['Edad'].mean()))
            print('El promedio de peso es: {}'. format(df['Peso'].mean()))
            print('El promedio de altura es: {}'. format(df['Altura'].mean()))
        else:
            print("Sin informacion para calcular")
    elif Sel==4:
        if llave==1:
            df2=df[["Nombre","Apellido","IMC"]]
            print(df2)
        else:
            print("Sin informacion para calcular")
    elif Sel==0:
        Ent=0
        print("Salir del programa")
    else:
        print("Número ingresado no aplica, elija uno nuevamente")

