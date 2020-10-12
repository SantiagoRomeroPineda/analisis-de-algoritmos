def cortes(x=3,y=5):
    matriz=[[0 for j in range(x+1)]for i in range(y+1)]
    for i in range(1,y+1):
        for j in range(1,x+1):
            if i!=j:
                respuesta=1e8
                for k in range(1,j):
                    respuesta=min(respuesta, 1 + matriz[i][j-k] + matriz[i][k])
                for k in range(1,i):
                    respuesta=min(respuesta, 1 + matriz[i-k][j] + matriz[k][j])
                matriz[i][j]=respuesta
    
    return matriz[y][x]

print(cortes())