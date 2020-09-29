
"""
    Realizado por:
    Santiago Romero
    Davis Steven Lopez Tobar 
"""
import time
start_time = time.time()
print(time.ctime( start_time) )

# arreglos con n digitos    Todos los digitos son 9 
arr10= [9 for i in range(10)]
arr100=[9 for i in range(100)]
arr1000=[9 for i in range(1000)]
arr2000=[9 for i in range(2000)]


def organizarSuma(arr=[],arr2=[]):
    if len(arr2)>len(arr):
        return suma(arr2,arr)
    return suma(arr,arr2)

def suma(arr,arr2):
    i,j=len(arr)-1, len(arr2)-1
    residuo=0
    arreglo=[]                                                   
    while i>=0:
        if(j<0):
            aux =arr[i]+residuo
        else:  
            aux =arr[i]+arr2[j]+residuo
        arreglo.insert(0,aux%10)
        residuo= (aux//10)
        i-=1
        j-=1
    if residuo != 0:
        arreglo.insert(0,residuo)
    return arreglo

def multiplicacion(arr,arr2):
    total=[]
    ceros=[]
    contador=0
    for i in range(len(arr)-1,-1,-1):
        suma=[]
        residuo=0
        for j in range(len(arr2)-1,-1,-1):
            aux =(arr[i]*arr2[j])+residuo
            contador+=1
            suma.insert(0,aux%10)
            residuo= (aux//10)
        if residuo != 0:
            suma.insert(0,residuo)
        total=(organizarSuma(total,suma+ceros)) #aqui se llama a la función sumar
        ceros.append(0)
    return total

print(multiplicacion([9,9],[9,9]))
    
print(organizarSuma(arr10,arr10))
print("--- %s seconds ---" % (time.time() - start_time))