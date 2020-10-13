def cutRod(n, valores):
    arreglo=[0 for i in range(n+1)]
    for i in range(1,n+1):
        maximo=0
        for j in range(i):
            maximo=max(maximo, valores[j]+arreglo[j-i-1])
        arreglo[i]=maximo
    return arreglo[n]
print(cutRod(3,[3,5,8]))