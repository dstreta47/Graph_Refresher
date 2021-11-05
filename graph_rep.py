class AdjNode:
    def __init__(self,data):
        self.vertex = data
        self.next = None


class graph:
    def __init__(self,vertex):
        self.V = vertex
        self.graph = [None] * self.V


    def add_edge(self,src,dest):    
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] =node

V =5
g = graph(V)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(0,3)        
