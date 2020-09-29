"""
    Realizado por 
        santiago Romero Pineda
        David Lopez
"""

import random
def quicksort(lista):
    if len(lista)==0 or len(lista)==1:
        return lista
    pivote = random.randrange(0,len(lista)-1)
    mayores=[]
    menores=[]
    iguales=[]
    for i in lista:
        if i > lista[pivote]:
            mayores.append(i)
        if i < lista[pivote]:
            menores.append(i)
        if i == lista[pivote]:
            iguales.append(i)
    return quicksort(menores) + iguales + quicksort(mayores)

print(quicksort([1,5,8,2,4,5,6]))