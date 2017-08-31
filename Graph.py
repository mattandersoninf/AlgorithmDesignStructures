# and an array of neighbor nodes
# Possibly set up a dictionary based on the values with the neighbors as the keys
# and the weighted paths represent the value parameter
class Vertex:
    def __init__(self,key):
        self.id = key
        self.neighborsList = {}

    def addNeighbor(self,nbr,weight=0):
        self.neighborsList[nbr] = weight

    def getConnections(self):
        return self.adjencyList.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.adjencyList[nbr]

# class structure for graph  
class Graph:
  def __init__(self, vertexDict = {}, directed = False):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    
  def addVertex(self, vertex):
    vertexDict[vertex.value] = vertex.neighbors
    
