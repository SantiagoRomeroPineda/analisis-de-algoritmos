import time
def mochilaF(peso, valor, pesoMaximo):
    filas= len(peso)+1
    columnas=pesoMaximo+1
    mochila= [[0 for i in range(columnas)] for j in range(filas)]
    for i in range(1,filas):
        for j in range(1,columnas):
            if peso[i-1] <= j:
                suma=valor[i-1]+ mochila[i-1][j-peso[i-1]]
                if mochila[i-1][j]>suma:
                    mochila[i][j]=mochila[i-1][j]
                else:
                    mochila[i][j]=suma
            else:
                mochila[i][j]=mochila[i-1][j]

    maleta=[]
    i=filas-1
    j=columnas-1

    pesoT = 0

    while(i>0):
        pesoT += peso[i-1]
        if pesoT <= pesoMaximo:
            maleta.append(i-1)
            i -= 1
            j -= peso[i-1]
        else:
            pesoT -= peso[i-1]
            i -= 1
    print(maleta)
              
valor=[2,2,4,5,3]    
peso=[3,1,3,4,2]

pesoMaximo=7
mochilaF(peso,valor, pesoMaximo)