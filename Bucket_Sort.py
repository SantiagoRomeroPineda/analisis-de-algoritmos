"""
    modificado por:
     Santiago romero Pineda
     David Lopez
"""
def bucket_sort(lista):
    masLargo = max(lista)
    longi = len(lista)
    size = masLargo/longi
    
 
    buckets = [[] for _ in range(longi)]
    for i in range(longi):
        j = int(lista[i]/size)
        if j != longi:
            buckets[j].append(lista[i])
        else:
            buckets[longi - 1].append(lista[i])
    
    for i in range(longi):
        insertion_sort(buckets[i])
    
    result = []
    for i in range(longi):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while (j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
 
 


arr1= [101, 32, 100, 200, 32, 10, 6, 4, 50, 9]
sorted_arr = bucket_sort(arr1)
print('Lista Ordenada: ',sorted_arr)






"""
referencia:
    https://www.geeksforgeeks.org/

"""

