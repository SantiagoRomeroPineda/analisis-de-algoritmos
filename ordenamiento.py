"""
    Realizado por 
        santiago Romero Pineda
        David Lopez
"""

def seleccion(arreglo):
    for i in range(0,len(arreglo)):
        menor =arreglo[i]
        pos = i
        for j in range(i,len(arreglo)):
            if arreglo[j]<menor:
                menor=arreglo[j]
                pos=j 
        v= arreglo[i]
        arreglo[i]=menor
        arreglo[pos]=v
    return arreglo

def burbuja(arreglo):
    for i in range(0,len(arreglo)):
        for j in range(1,len(arreglo)):
            if(arreglo[i]>arreglo[j]):
                v= arreglo[j]
                arreglo[j]=arreglo[i]
                arreglo[i]=v
    return arreglo
print(seleccion([5,2,3,1]))
print(burbuja([5,2,3,1]))