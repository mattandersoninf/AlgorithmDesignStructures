# class structure for vertex, utilizes the value parameter as the key
# and an array of neighbor nodes
# Set up the dictionary so that the Vertex will have a key parameter and 
# a dictionary of neighbors with the neighbor values as the keys
# and the weight to that neighbor as the associated value

class Vertex:
  # initializer for the dictionary which will use the vertex's id as the key value
  # use the neighborsList dictionary as  
  def __init__(self,key):
      self.id = key
      self.neighborsList = {}
      
  # add a neighbor by setting the key parameter in the neighbor list dictionary
  # with it's weight to getting to the key as the value associated in the dictionary
  def addNeighbor(self,nbr,weight=0):
      self.neighborsList[nbr] = weight

  # get all the neighbors associated with this vertex
  def getConnections(self):
      return self.adjencyList.keys()

  # return the vertex's object id
  def getId(self):
      return self.id
      
  # return the weight associated with a specific neighbor to this vertex    
  def getWeight(self,nbr):
      return self.adjencyList[nbr]

# class structure for graph  
class Graph:
  # utilize the dictionary to keep track of all the parameters within the Graph
  # eliminates the need for self.parameter = parameter for every parameter in the
  # initializer
  # use the matrix parameter to print out all of the vertices and edges for a visual
  # representation on the console
  def __init__(self, vertexDict = {}, matrix = None):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
  
  # add a vertex to the Graph  
  def addVertex(self, value):
    # you can't add values to a key in a dictionary if it already exists, so track
    # the Exception
    if value in self.vertexDict:
      raise Exception(str(value) + " is already in this Graph.")
    
    # given a key value, make a new vertex and treat that value as the key to connect to
    # that value
    newVertex = Vertex(value)
    self.vertexDict[value] = newVertex
    
  def addEdge(self, vertexKey1, vertexKey2, weight = 0):
    if vertexKey1 not in self.vertexDict:
      self.vertexDict[vertexKey1] = Vertex(vertexKey1)
    if vertexKey2 not in self.vertexDict:
      self.vertexDict[vertexKey2] = Vertex(vertexKey2)
    self.vertexDict[vertexKey1].addNeighbor(vertexKey2, weight)
    
  def getVertices(self):
    return self.vertexDict.keys()
    
  def getAllConnections(self):
    for v in range(len(vertexDict)):
      
    
  def addEdge(self, vertex):
    
