def subconjunto(arreglo):
    suma=sum(arreglo)
    K=suma//2
    tam=len(arreglo)
    if suma%2 !=0:
        return False
    matriz = [[False for x in range(K + 1)] for y in range(tam + 1)]
    for i in range(tam + 1):
        matriz[i][0] = True

    for i in range(1, tam + 1):
        for j in range(1, K + 1):
            if j <arreglo[i - 1] :
                matriz[i][j] = matriz[i - 1][j]
            else:

                matriz[i][j] = matriz[i - 1][j] or matriz[i - 1][j - arreglo[i - 1]]


    return matriz[tam][K]


arreglo = [2, 1, 1, 1, 3, 2]
print(subconjunto(arreglo))




#referencaias 