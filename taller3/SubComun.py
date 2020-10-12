palabra1="AGGTAB"
palabra2="GXTXAYB"
def subsecuencia(palabra1, palabra2):
    longitud1= len(palabra1)+1
    longitud2= len(palabra2)+1
    matriz = [[0 for j in range(longitud1)]for i in range(longitud2)]
    for i in range(1,longitud2):
        for j in range(1,longitud1):
            if palabra1[j-1] == palabra2[i-1] :
                matriz[i][j]+=1+matriz[i-1][j-1]
            else:
                matriz[i][j]+=max(matriz[i-1][j],matriz[i][j-1])
    subsecuencia=""
    j=longitud1-1
    i=longitud2-1
    while i>=1:
        if matriz[i-1][j]<matriz[i][j]:
            subsecuencia+=(palabra2[i-1])
            j-=1
            i-=1
        i-=1

    print(subsecuencia[::-1])        
    for a in matriz:
        for b in a:
            print(b,end =" ")
        print()
    print("\n")

subsecuencia(palabra1, palabra2)
