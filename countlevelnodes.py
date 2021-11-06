from collections import defaultdict

class graph:
    def  __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s, l):	
        V = 10
        visited = [False] * V
        level = [0] * V
        for i in range(V):
            visited[i] = False
            level[i] = 0
        queue = []
        visited[s] = True
        queue.append(s)
        level[s] = 0
        while (len(queue) > 0):
            s = queue.pop(0)
            for i in self.graph[s]:
                if (not visited[i]):
                    level[i] = level[s] + 1
                    visited[i] = True
                    queue.append(i)
        count = 0
        for i in range(V):
            if (level[i] == l):
                count += 1
        return count


g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
level = 2
print(g.BFS(0, level))
