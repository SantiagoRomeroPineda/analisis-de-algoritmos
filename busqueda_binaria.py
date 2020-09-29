"""
    Realizado por 
        santiago Romero Pineda
        David Lopez
"""
def busquedaBinaria(lista, x):
    if not lista:
        return False
    pivote = len(lista)//2
    if(lista[pivote]==x):
        return True
    elif lista[pivote]<x:
        return busquedaBinaria(lista[pivote+1:], x)
    else:
        return busquedaBinaria(lista[0:pivote],x)

print(busquedaBinaria([1,2,3,4,5,6,7,8,9],10))
