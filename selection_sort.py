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
print(seleccion([5,2,3,1]))