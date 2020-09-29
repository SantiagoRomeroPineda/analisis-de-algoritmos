import random
import time
"""
 modificado por 
 Santiago Romero Pineda
 David Lopez
"""

lista= [random.randrange(0,10) for i in range(10)]
def counting_sort(lista, mayor):
    auxiliar = [0]*(mayor + 1)
    for i in range(len(lista)):
        auxiliar[lista[i]] = auxiliar[lista[i]] + 1
 
    auxiliar[0] = auxiliar[0] - 1
    for i in range(1, mayor + 1):
        auxiliar[i] = auxiliar[i] + auxiliar[i - 1]
 
    result = [None]*len(lista)
 
    for i in reversed(lista):
        result[auxiliar[i]] = i
        auxiliar[i] = auxiliar[i] - 1
 
    return result
 
print(counting_sort(lista,max(lista)))


"""
    referencia:
    www.sanfoundry.com

"""
