"""
    Realizado por 
        santiago Romero Pineda
        David Lopez
"""

#ejercicio 2.15"
"""
Respuesta

Este es el método que se implementa en quicksort, sin embargo, varias formas de hacerlo,
una de ellas es organizando e intercambiando posiciones dentro del mismo arreglo o creando 3 arreglos más
*uno para los mayores
*otro para los iguales (aunque este no es tan necesario)
*otro para los iguales

Este ejecicio lo haré intercalando las posiciones en el arreglo original para no gastar mas memoria

"""
#v será el pivote
def split(a, v):
    pivote = 0
    n= len(a)
    for i in range(0,n):
        if a[i] < v:
            a[i], a[pivote] = a[pivote], a[i]
            pivote = pivote +1
    for i in range(pivote,n):
        if a[i] == v:
            a[i], a[pivote] = a[pivote], a[i]
            pivote = pivote +1
    return a

print("punto 2.15")
print("In our median-finding algorithm (Section 2.4), a basic primitive is the split operation,  which takes as input an array S and a value v and then divides S into three sets: the elements less than v, the elements equal to v, and the elements greater than v. Show how to implement this split operation in place, that is, without allocating new memory.")
print("original: [7,2,6,0,1,45] ")
print ("utilizando función split: ",split([7,2,6,0,1,45],0), "\n")


#punto 2.16
print("punto 2.16")
print("You are given an infinite array A[] in which the first n cells contain integers in sorted order and the rest of the cells are filled with ∞. You are not given the value of n. Describe an algorithm that takes an integer x as input and finds a position in the array containing x, if such a position exists,in O(logn) time.  (If you are disturbed by the fact that the array A has infinite length,assume instead that it is of length n, but that you don't know this length, and that the implementation of the array data type in your programming language returns the error message 1 whenever elements A[i] with i > n are accessed.)")

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

print("buscar 10 en [1,2,3,4,5,6,7,8,9]")
print(busquedaBinaria([1,2,3,4,5,6,7,8,9],10),"\n")


#punto 2.17
print("punto 2.17")
print("Givena sorted array of distinct integers A[1;:::;n], you want to find out whether there is an index i for which A[i] =i. Givea divide-and-conquer algorithm that runs in time O(log n)")
def no_se_como_llamarle(lista):
    
    mitad=len(lista)//2
    if(mitad==0):
        return False
    if lista[mitad]==mitad:
        return True
    if lista[mitad]> mitad:
        return  no_se_como_llamarle(lista[0:mitad])
    elif lista[mitad] <mitad:
        return  no_se_como_llamarle(lista[mitad+1:])
    else:
        return False
        
print("arrego [1,2,3,3,5,6,7]")
print("el numero 3 se encuentra en la posicion 3?: ",no_se_como_llamarle([1,2,3,3,5,6,7]),"\n")