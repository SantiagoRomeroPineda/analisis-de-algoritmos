def selectionSort(lista):
    if len(lista)<=1:
        return lista
    else:
        for i in range(0,len(lista)):
            if lista[0]>lista[i]:
                temp=lista[0]
                lista[0]=lista[i]
                lista[i]=temp
        return lista[0:1]+selectionSort(lista[1:])


print(selectionSort([4,3,5,2,1]))

# T.E =  n= len(lista)
# O.B = (it is 1)
# T(n) = n + T(n-1)
# S(n) = n+1  + S(n-1)