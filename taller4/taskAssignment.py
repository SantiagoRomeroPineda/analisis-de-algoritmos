from Vertice import Vertex
from Grafo import Graph


"""

Asignación de labores ([Boh92], ejercicio 7.6)

No logramos terminarlo del todo, pero el codigo es una aproximación a lo
creemos que es la solución.

"""

grafo = Graph()
for i in range(1,10):
    grafo.addVertex(Vertex(i))
grafo.taskAssignment()