arreglo= [ 8, 15, 3, 7 ]
def cartas(arreglo):
    n=len(arreglo)
    matriz = [[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        matriz[i][i]=arreglo[i]
    
    for corrimiento in range(1,n):
        i =0
        for j in range (corrimiento, n):
            #i= j-corrimiento
            #f1 = (i+2,j)
            #f2 = (i+1,j-1)
            #f3 = (i, j-2)
            f1 = 0
            f2 = 0
            f3 = 0
            if((i + 2) <= j): 
                f1 = matriz[i + 2][j] 
            if((i + 1) <= (j - 1)): 
                f2 = matriz[i + 1][j - 1] 
            if(i <= (j - 2)): 
                f3 = matriz[i][j - 2] 
            matriz[i][j] = max(arreglo[i] + min(f1, f2),arreglo[j] + min(f2, f3))
            i+=1
            for a in matriz:
              for b in a:
                  print(b,end =" ")
              print()
            print("\n")
    return matriz[0][n-1]
print("el jeugo perfecto sumaría: ",cartas(arreglo))

