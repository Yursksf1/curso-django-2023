a=""
q=1
Nombre=[]
Nom=a
while q!=0:
  print("Cual es tu nombre")
  q=input()
  if q=="0":
     break
  else: print("hola {}".format(q))
  Nombre.append(q)
print("la cantidad de pesonas saludadas son: {}".format(len(Nombre))) 

for i in Nombre:
     a=a+"-"
     print(" {} Adios {} hasta pronto!".format(a,i))
a="*"
b=""
cont=0
for i in Nombre:
     cont=cont+1
     w=cont%2
     if w==0:
      a="*"*cont
      print(" {} Adios {} hasta pronto!".format(a,i))
     else:
      b="-"*cont
      print(" {} Adios {} hasta pronto!".format(b,i))
