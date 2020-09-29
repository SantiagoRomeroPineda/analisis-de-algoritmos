"""
 Realizado por 
 Santiago Romero Pineda
"""

def merge_sort(lista):

   if len(lista) < 2:
      return lista
    
   else:
        mitad = len(lista) // 2
        right = merge_sort(lista[:mitad])
        left = merge_sort(lista[mitad:])
        return intercalar(right, left)
    
# Función merge
def intercalar(lista1, lista2):

    i, j = 0, 0 
    resultado = [] 
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
 
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

# Prueba del algoritmo

lista = [100,31,3,88,1,4,2,42]

merge_sort_result = merge_sort(lista)  
print(merge_sort_result)

