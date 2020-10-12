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
            if((i + 2) <= j): 
                f1 = matriz[i + 2][j] 
            f2 = 0
            if((i + 1) <= (j - 1)): 
                f2 = matriz[i + 1][j - 1] 
            f3 = 0
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




# arreglo= [ 8, 15, 3, 7 ]
# #arreglo=[ 20, 30, 2, 2, 2, 10] 
# def cartas(arreglo):
#     n=len(arreglo)
#     matriz = [[0 for i in range(n)]for i in range(n)]
#     for i in range(n):
#         matriz[i][i]=arreglo[i]
#     aux=n-1
#     for j in range(1,n):
#         count=0
#         for i in range(0,aux):
#             # matriz[i][j+cont]=1
#             I1=0
#             J1=0
#             I2=0
#             J2=0
#             if  i+1<n:
#                 I2=i+1
#             if i+2<n:
#                 I1=i+2
#             if j+count-1>-1:
#                 J1=j+count-1
#             if j+count-2>-1:
#                 J2=j+count-2
#             val1=arreglo[1]+min(matriz[I1][j+count],matriz[I2][J1])
#             val2=arreglo[j]+min(matriz[i][J2],matriz[I2][J1])
#             print(arreglo[i]," ",arreglo[j])
#             matriz[i][j+count]=max(val1,val2)
#             for a in matriz:
#                 for b in a:
#                     print(b,end =" ")
#                 print()
#             print("\n")
#             count+=1
#         aux-=1




#     # for i in range(n):
#     #     var=0
#     #     for j in range(i,n):
#             # I1=0
#             # J1=0
#             # I2=0
#             # J2=0
#             # if  i+1<n:
#             #     I2=i+1
#             # if i+2<n:
#             #     I1=i+2
#             # if j-1>-1:
#             #     J1=j-1
#             # if j-2>-1:
#             #     J2=j-2
            
#     #         val1=arreglo[i]+min(matriz[I1][j],matriz[I2][J1])
#     #         val2=arreglo[j]+min(matriz[i][J2],matriz[I2][J1])
#     #         print(val1," ",val2," ",max(val1,val2))
#     #         matriz[i][j]=max(val1,val2)
#     #         for a in matriz:
#     #             for b in a:
#     #                 print(b,end =" ")
#     #             print()
#     #         print("\n")

# cartas(arreglo)

