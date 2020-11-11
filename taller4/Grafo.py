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
    
    def connection(self,v1,v2, weigth=0):
        if (v1 in self.edges.keys() and v1 in self.edges.keys() ):
            if  v2 in self.edges[v1].keys():
                return False
            self.edges[v1].update({v2:weigth})
            return True
        return False

    def vertex_neighbours(self, v):
        return self.edges[v].keys()

    def edgeCost(self, v1, v2):
        return self.edges[v1].get(v2)

    # def DFS(self, v):
    #     for i in self.vertices.keys():
    #         self.vertices[i].mark=False
    #     stack = [v]
        
    #     while len(stack)!=0:
    #         for i in 



                
                


    
        


            

vertice = Vertice(1,12)
grafo = Graph()
print(grafo.addVertex(vertice))
vertice = Vertice(2,4)
print(grafo.addVertex(vertice))
vertice = Vertice(3,6)
print(grafo.addVertex(vertice))
print(grafo.connection(1,2,7))
print(grafo.connection(1,3))
print(grafo.edges)
print(grafo.vertex_neighbours(1))
print(grafo.edgeCost(1,2))



#     abc.abstractclassmethod
#     def veinosDeVertice(self, vertice):
#         pass
#     abc.abstractclassmethod
#     def costoArista(self):
#         pass
#     abc.abstractclassmethod
#     def DFS(self, vertice):
#         for i in self.vertices:
#             i.marca=False
        
#    def DFSUtil(self, v): 
#         self.vertices[v].marca = True

#         for i in self.graph[v]: 
#             if visited[i] == False: 
#                 self.DFSUtil(i, visited) 

        
#     abc.abstractclassmethod
#     def busquedaAnchura(self):
#         pass
#     abc.abstractclassmethod
#     def dijkstra(self):
#         pass
#     abc.abstractclassmethod
#     def bellman_Ford(self):
#         pass
#     abc.abstractclassmethod
#     def prim(self):
#         pass
#     abc.abstractclassmethod
#     def Kruskal(self):
#         pass

        
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

