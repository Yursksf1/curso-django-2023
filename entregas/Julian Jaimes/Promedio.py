sum=0
Prom=[1,2,3,4,4,5,6,7,8,4,3,2,4,4,4,5,6,7,2]
for i in Prom:
    sum=sum+i
    print(sum)
n=len(Prom)
print(" El valor del promedio es {} y contiene {} datos" .format(sum/n,n))
