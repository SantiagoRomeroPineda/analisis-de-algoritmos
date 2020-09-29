def factorial(n):
    return (1 if (n<=1) else (n*factorial(n-1)))

print (factorial(4))

def fibo(n):
    return (n if (n<=1) else (fibo(n-1)+fibo(n-2)))
print (fibo(6))

def sumaLista(lista):
    return (0 if not lista else (lista[0] + sumaLista(lista[1:]))  )
print(sumaLista((1,2,3,4,5)))

def par_impar(n):
    return (True if n==0 else (not par_impar(n-1)))

print(par_impar(10))