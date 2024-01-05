class Graph:
    def __init__(self):
        self.adjacencyList = {}
    
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
            
    def printGraph(self):
        for vertex in self.adjacencyList:
            print(vertex,":",self.adjacencyList[vertex])
            
            
customGraph = Graph()
customGraph.addVertex("A")
customGraph.addVertex("B")
customGraph.addVertex("C")
customGraph.addVertex("D")
customGraph.addEdge("A","B")
customGraph.addEdge("C","B")
customGraph.addEdge("A","C")
customGraph.addEdge("D","C")
customGraph.addEdge("A","D")
customGraph.printGraph()
# customGraph.removeEdge("A","C")
print('-----------------------------------------------')
customGraph.removeVertex("D")
customGraph.printGraph()
