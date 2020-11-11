"""
Made and modified by:
    Santiago Romero
    David Lopez
"""

import abc
import math
from abc import ABCMeta
from Vertice import Vertice


class Graph:
    __metaclass__ = ABCMeta
    def __init__(self):
        self.vertices={}
        self.edges={}
        self.matrix=[]
        self.adjacency_list=[]

    def addVertex(self,v):
        if v.id in self.edges.keys():
            return False
        self.vertices[v.id]=v
        self.edges[v.id]={}
        return True
    
    def restartVertices(self):
        for i in self.vertices.keys():
            self.vertices[i].mark=False

    def connectionMatrix(self, v1,v2, weigth=1):
        tam=max(v1,v2)
        if len(self.matrix)<tam:
            
            val=len(self.matrix)
            for i in range(len(self.matrix),tam):
                self.matrix.append([0]*tam)
            for i in range(0,val):
                for j in range(val,tam):
                    self.matrix[i].append(0)
        
        self.matrix[v1-1][v2-1]=weigth
        self.matrix[v2-1][v1-1]=weigth

    
    def connection(self,v1,v2, weigth=1):
        if (v1 in self.edges.keys() and v2 in self.edges.keys() ):
            if  v2 in self.edges[v1].keys():
                return False
            if v1 in self.edges[v2].keys():
                return False
            self.edges[v1].update({v2:weigth})
            self.edges[v2].update({v1:weigth})
            self.connectionMatrix(v1,v2,weigth)
            self.adjacency_list.append([v1,v2, weigth])
            self.adjacency_list.append([v2,v1, weigth])
            return True
        return False

    def printMatrix(self):
        for i in self.matrix:
            for j in i:
                print(j,end="\t")
            print()
        print()    

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
                    print(value,"->",i,end=", ")
                    output.append(i)
                    stack.append(i)
                    break
                else:
                    stack.pop()
        return output

    def BFS(self,v):
        self.restartVertices()
        queue = [v]
        output = [v]
        while len(queue)!=0:
            self.vertices[queue[0]].mark=True
            value=queue[0]
            queue.pop(0)
            for i in self.edges[value].keys():
                if not i in queue:
                    if self.vertices[i].mark==False:
                        queue.append(i)
                        print(value,"->",i,end=", ")
                        output.append(i)
        return output

 

    def minDistance(self, distances, marked): 
        min = math.inf 
        for v in range(len(self.vertices)): 
            if distances[v] < min and not marked[v] : 
                min = distances[v] 
                min_index = v 
        return min_index 


    def dijkstra(self, src): 
        nVertices=len(self.vertices)
        distances = [math.inf] *  nVertices
        distances[src-1] = 0
        marked = [False] * nVertices
   
        for _ in range(nVertices): 
            u = self.minDistance(distances, marked) 
            marked[u] = True 
            for v in range(nVertices): 
                if self.matrix[u][v] > 0 and not marked[v]  and distances[v] > distances[u] + self.matrix[u][v]: 
                    distances[v] = distances[u] + self.matrix[u][v] 
        return distances 


            
    def bellmanFord(self, src):  
        nVertices=len(self.vertices)
        distances = [math.inf] * nVertices  
        distances[src-1] = 0

        for _ in range(nVertices - 1):    
            for v1, v2, weigth in self.adjacency_list:  
                if distances[v1-1] != math.inf and distances[v1-1] + weigth < distances[v2-1]:  
                        distances[v2-1] = distances[v1-1] + weigth  
  

        for v1, v2, weigth in self.adjacency_list:  
                if distances[v1-1] != math.inf and distances[v1-1] + weigth < distances[v2-1]:  
                        return False
                          
        return distances

    def printPrim(self, parent): 
        for i in range(1, len(self.vertices)): 
            print (parent[i]+1, "->", i+1, "\t", self.matrix[i][ parent[i] ] )

    def prim(self): 
        nVertices=len(self.vertices)
        distances = [math.inf] * nVertices
        parent = [None] * nVertices
        distances[0] = 0 
        marked = [False] * nVertices
        parent[0] = -1
        for _ in range(nVertices): 
            u = self.minDistance(distances, marked) 
            marked[u] = True
            for v in range(nVertices): 
                if self.matrix[u][v] > 0 and not marked[v] and distances[v] > self.matrix[u][v]: 
                        distances[v] = self.matrix[u][v] 
                        parent[v] = u 
        return parent

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.adjacency_list = sorted(self.adjacency_list, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(len(self.vertices)):
            parent.append(node)
            rank.append(0)
        while e < len(self.vertices) - 1:
            u, v, w = self.adjacency_list[i]
            i = i + 1
            x = self.find(parent, u-1)
            y = self.find(parent, v-1)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        return result
                
            

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
print(grafo.DFS(2))
print(grafo.BFS(2))
grafo.printMatrix()
print(grafo.dijkstra(2))
print(grafo.bellmanFord(2))
grafo.printPrim(grafo.prim()) 
print(grafo.kruskal())

   


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




"""
References:
    - www.programiz.com
    - www.geeksforgeeks.org
"""

        

