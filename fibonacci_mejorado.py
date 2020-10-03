def fibo(n,mapa = {0: 0, 1: 1}):
    if n not in mapa:
        mapa[n] = fibo(n-1, mapa) + fibo(n-2, mapa)
    return mapa[n]
#print(fibo(7))

def fibon(n,arreglo = [0,1]):
    if len(arreglo)<n:
        arreglo.append(fibon(n-1, arreglo) + arreglo[n-2]) 
    return arreglo[n-1]
#print(fibon(5))
def fib (n, lista=[0,1]):
    for i in range(2,n+1):
            lista.append(lista[i-1]+lista[i-2])
    return lista[n]
print(fib(22))

def fibonacci(n,antepenultimo=0, penultimo=1):
    if n<2:
        return n
    ultimo= 0
    for i in range(0,n+1):
        ultimo = antepenultimo+ultimo
        antepenultimo=penultimo
        penultimo=ultimo
    return ultimo
print(fibonacci(22)) 
        
        
