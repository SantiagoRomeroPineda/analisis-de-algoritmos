import numpy

def fibonacci(n): 	
	Q = [[1, 1], 
		[1, 0]] 
	if (n == 0): 
		return 0
	potencia(Q, n - 1) 		
	return Q[0][0] 
	
def multiplicar(Q, M): 
	x = (Q[0][0] * M[0][0] + Q[0][1] * M[1][0]) 
	y = (Q[0][0] * M[0][1] + Q[0][1] * M[1][1]) 
	z = (Q[1][0] * M[0][0] + Q[1][1] * M[1][0]) 
	w = (Q[1][0] * M[0][1] + Q[1][1] * M[1][1]) 
	Q[0][0] = x 
	Q[0][1] = y 
	Q[1][0] = z 
	Q[1][1] = w 
			
def potencia(Q, n): 
	if( n == 0 or n == 1): 
		return 
	M = [[1, 1], 
		[1, 0]] 
	potencia(Q, n // 2)
	multiplicar(Q, Q)
	if (n % 2 != 0): 
		multiplicar(Q, M)  

n = 22
print(fibonacci(n)) 

"""
	Referencia:
	https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
"""