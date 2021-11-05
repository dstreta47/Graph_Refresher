from collections import defaultdict

class graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


    def bfs(self,s):
        visited = [False] * (max(self.graph)+1)
        queue = []
        visited[s] = True
        queue.append(s)
        while queue:
            a = queue.pop(a)
            print(a)
            for i in self.graph[s]:
                if visited[s] == False:
                    queue.append(i)
                    visited[i] = True     


g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)  
g.BFS(2)                     
