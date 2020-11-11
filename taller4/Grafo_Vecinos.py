class Vertice:
    def __init__(self, value):
        self.vertice = value
        self.next = None

class Grafo_Vecinos():
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = Vertice(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = Vertice(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")