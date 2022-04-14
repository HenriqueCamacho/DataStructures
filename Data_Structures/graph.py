#Undirected graph
class Graph():
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vtxname):
        self.adjacencyList.setdefault(vtxname, [])
        
    def addEdge(self, vtx1, vtx2):
        self.adjacencyList[vtx1].append(vtx2)
        self.adjacencyList[vtx2].append(vtx1) 
        
    def removeEdge(self, vtx1, vtx2):
        self.adjacencyList[vtx1].remove(vtx2)    
        self.adjacencyList[vtx2].remove(vtx1)
        
    def removeVertex(self, vtx):
        #print("Elements of "+str(self.adjacencyList[vtx]) )
        while len(self.adjacencyList[vtx] )>0: 
            self.removeEdge(vtx, self.adjacencyList[vtx][0] )
        self.adjacencyList.pop(vtx, None)       
 
gp = Graph()
gp.addVertex("Tokyo")
gp.addVertex("São Paulo")       
gp.addVertex("New York")
gp.addVertex("London")
gp.addVertex("Buenos Aires")
gp.addVertex("Paris")
gp.addVertex("Berlim")
gp.addVertex("Beijing")
gp.addEdge("Tokyo","São Paulo")
gp.addEdge("Tokyo","Paris")
gp.addEdge("São Paulo","Berlim")
gp.addEdge("London","Buenos Aires")
#print(gp.adjacencyList)
#gp.removeEdge("São Paulo", "Tokyo")
gp.addEdge("Tokyo","Berlim")
gp.addEdge("Tokyo","Beijing")
print(gp.adjacencyList)
gp.removeVertex("Tokyo")
print(gp.adjacencyList)
