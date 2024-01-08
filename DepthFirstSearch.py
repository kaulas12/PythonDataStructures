class Graph:
    def __init__(self):
        self.adjacencyList = {}
        
    def printGraph(self):
        for vertex in self.adjacencyList:
            print(vertex,":",self.adjacencyList[vertex])
    
    def addVertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []
            return True
        return False
    
    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacencyList.keys() and vertex2 in self.adjacencyList.keys():
            self.adjacencyList[vertex1].append(vertex2)
            self.adjacencyList[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacencyList.keys() and vertex2 in self.adjacencyList.keys():
            self.adjacencyList[vertex1].remove(vertex2)
            self.adjacencyList[vertex2].remove(vertex1)
            return True
        return False
            
    def removeVertex(self,vertex):
        if vertex in self.adjacencyList.keys():
            for other_vertex in self.adjacencyList[vertex]:
                self.adjacencyList[other_vertex].remove(vertex)
            del self.adjacencyList[vertex]
        return True
    
    def bfs(self,vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            current_vertex = queue.pop(0)
            print(f'{current_vertex}')
            for adjVertex in self.adjacencyList[current_vertex]:
                if adjVertex not in visited:
                    visited.add(adjVertex)
                    queue.append(adjVertex)
                    
    def dfs(self,vertex):
        visited = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(f'{current_vertex}')
                visited.add(current_vertex)
                for adjVertex in self.adjacencyList[current_vertex]:
                    stack.append(adjVertex)
                    
                
                
                
                
                    
            
            
customGraph = Graph()
customGraph.addVertex("A")
customGraph.addVertex("B")
customGraph.addVertex("C")
customGraph.addVertex("D")
customGraph.addVertex("E")
customGraph.addEdge("A","B")
customGraph.addEdge("E","B")
customGraph.addEdge("A","C")
customGraph.addEdge("D","E")
customGraph.addEdge("C","D")
customGraph.printGraph()
customGraph.dfs("A")
