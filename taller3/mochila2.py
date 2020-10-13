import time
def mochila(peso, valor, pesoMaximo):
    filas= len(peso)+1
    columnas=pesoMaximo+1
    matriz= [[0 for i in range(columnas)] for j in range(filas)]
    for i in range(1,filas):
        for j in range(1,columnas):
            if peso[i-1] <= j:
                matriz[i][j]=max(valor[i-1]+ matriz[i-1][j-peso[i-1]],matriz[i-1][j])
            else:
                matriz[i][j]=matriz[i-1][j]
    for a in matriz:
        for b in a:
            print(b,end =" ")
        print()


              
valor=[2,2,4,5,3]    
peso=[3,1,3,4,2]

pesoMaximo=7
mochila(peso,valor, pesoMaximo)