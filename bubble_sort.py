"""
    Realizado por 
        santiago Romero Pineda
        David Lopez
"""

def burbuja(arreglo):
    for i in range(0,len(arreglo)):
        for j in range(0,len(arreglo)):
            if(arreglo[i]<arreglo[j]):
                v= arreglo[j]
                arreglo[j]=arreglo[i]
                arreglo[i]=v
    return arreglo

print(burbuja([5,2,3,1]))