import abc
from abc import ABCMeta
from Vertice import Vertice

class Graph:
    __metaclass__ = ABCMeta
    def __init__(self):
        self.vertices={}
        self.edges={}

    def addVertex(self,v):
        if v.id in self.edges.keys():
            return False
        self.vertices[v.id]=v
        self.edges[v.id]={}
        return True
    
    def restartVertices(self):
        for i in self.vertices.keys():
            self.vertices[i].mark=False

    def connection(self,v1,v2, weigth=0):
        if (v1 in self.edges.keys() and v2 in self.edges.keys() ):
            if  v2 in self.edges[v1].keys():
                return False
            if v1 in self.edges[v2].keys():
                return False
            self.edges[v1].update({v2:weigth})
            self.edges[v2].update({v1:weigth})
            return True
        return False

    def vertex_neighbours(self, v):
        return self.edges[v].keys()

    def edgeCost(self, v1, v2):
        return self.edges[v1].get(v2)

    def DFS(self, v):
        self.restartVertices()
        stack = [v]
        output =[v]        
        while len(stack)!=0:
            self.vertices[stack[-1]].mark=True
            value=stack[-1]
            
            for i in self.edges[value].keys():
                if not self.vertices[i].mark:
                    print(value," -> ",i)
                    output.append(i)
                    stack.append(i)
                    break
                else:
                    stack.pop()
        return output

    def BFS(self):
        self.restartVertices()
        

    def dijkstra(self):
        pass
    def bellman_Ford(self):
        pass
    def prim(self):
        pass
    def Kruskal(self):
        pass
                
                


    
        


            

vertice = Vertice(1,12)
grafo = Graph()
print(grafo.addVertex(vertice))
vertice = Vertice(2,4)
print(grafo.addVertex(vertice))
vertice = Vertice(3,6)
print(grafo.addVertex(vertice))
vertice = Vertice(4,"pepe")
(grafo.addVertex(vertice))
(grafo.connection(1,2,7))
(grafo.connection(1,3))
(grafo.connection(2,4))

print(grafo.edges)
(grafo.vertex_neighbours(1))
(grafo.edgeCost(1,2))
grafo.DFS(2)



 
#    def DFSUtil(self, v): 
#         self.vertices[v].marca = True

#         for i in self.graph[v]: 
#             if visited[i] == False: 
#                 self.DFSUtil(i, visited) 

        


        
# 1. Construya la clase Vertice.  Deje campos para el contenido y otras cosas exigidas por los algoritmos.
# 2. Construya la clase abstracta Grafo.  En esta clase deben aparecer los siguientes métodos:
# 	- Vecinos de un vértice (abstracto).
# 	- Costo de una arista (abstracto).
# 	- Búsqueda en profundidad.
# 	- Búsqueda en anchura.
# 	- Dijkstra.
# 	- Bellman-Ford
# 	- Prim
# 	- Kruskal
# Los métodos que no son abstractos deben ser agnósticos a la implementación particular del grafo.
# 3. Construya las tres implementaciones del grafo en sendas clases que hereden de la clase Grafo del punto anterior.  Se deben construir:
# 	- Grafo con matriz de adyacencias.
# 	- Grafo con lista de vecinos de cada vértice.
# 	- Grafo con lista de aristas.
# 4. Construya soluciones a los siguientes problemas de aplicación.  La clase que resuelve cada problema debe heredar de alguna de las implementaciones del punto anterior:
# 	- Ubicar 4 damas en un tablero de ajedrez de 4x4 ([Boh92], sección 7.1)
# 	- Asignación de labores ([Boh92], ejercicio 7.6)
# 	- Ejercicios 4.20, 4.21 y 5.26 de [Das08]

