"""
Ejercicio 4.20
Dasgupta
"""
import math
from Vertice import Vertex
from Grafo import Graph

grafo = Graph()
for i in range(1,6):
    grafo.addVertex(Vertex(i))

grafo.connection(1,2,4)
grafo.connection(2,3,2)
grafo.connection(3,5,5)
grafo.connection(3,4,2)


roads=[[5,1,2],[2,5,1]]
minimo=[math.inf]
for v1,v2,weigth in roads:
    aux=grafo.Roads(v1,v2,weigth)
    if aux <=minimo[0]:
        minimo=[aux,v1,v2]
print("la ruta mas optima es de la cidad: ",minimo[1]," a: ",minimo[2])
        




# 4. Construya soluciones a los siguientes problemas de aplicación.  La clase que resuelve cada problema debe heredar de alguna de las implementaciones del punto anterior:
# 	- Ubicar 4 damas en un tablero de ajedrez de 4x4 ([Boh92], sección 7.1)
# 	- Asignación de labores ([Boh92], ejercicio 7.6)
# 	- Ejercicios 4.20, 4.21 y 5.26 de [Das08]

