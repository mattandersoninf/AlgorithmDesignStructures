# class structure for vertex, utilizes the value parameter as the key
# and an array of neighbor nodes
# Set up the dictionary so that the Vertex will have a key parameter and 
# a dictionary of neighbors with the neighbor values as the keys
# and the weight to that neighbor as the associated value

class Vertex:
      # initializer for the dictionary which will use the vertex's id as the key value
      # use the neighborsList dictionary as  
      def __init__(self, key, visited = False):
          self.id = key
          self.neighborsList = {}
          self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
          
      # add a neighbor by setting the key parameter in the neighbor list dictionary
      # with it's weight to getting to the key as the value associated in the dictionary
      def addNeighbor(self, nbr, weight = 0):
          self.neighborsList[nbr] = weight
    
      # get all the neighbors associated with this vertex
      def getConnections(self):
          return list(self.neighborsList.keys())
    
      # return the vertex's object id
      def getId(self):
          return self.id
          
      # return the weight associated with a specific neighbor to this vertex    
      def getWeight(self,nbr):
          return self.neighborsList[nbr]
      
      def setVisitTrue(self):
          self.visited = True
          
      def setVisitFalse(self):
          self.visited = False

# class structure for graph  
class Graph(object):
  # utilize the dictionary to keep track of all the parameters within the Graph
  # eliminates the need for self.parameter = parameter for every parameter in the
  # initializer
  # use the matrix parameter to print out all of the vertices and edges for a visual
  # representation on the console
  def __init__(self, vertDict = {}):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
  
  # add a vertex object to vertexDict in the Graph class 
  def addVertex(self, value):
    # you can't add values to a key in a dictionary if it already exists, so track
    # the Exception
    if value in self.vertDict:
      raise Exception(str(value) + " is already in this Graph.")
    # given a key value, make a new vertex and treat that value as the key to connect to
    # that value
    newVertex = Vertex(value)
    self.vertDict[value] = newVertex
    
  # Add an edge to the Graph class, inputs should be 2 integer values
  # A weight can be specified to the path otherwise the weight will be 
  # set to 0  
  def addEdge(self, vertexKey1, vertexKey2, weight = 0):
    # If the specified vertex values aren't in the Graph already
    # add them to the vertexDict
    if vertexKey1 not in self.vertDict:
      self.addVertex(vertexKey1)
    if vertexKey2 not in self.vertDict:
      self.addVertex(vertexKey2)
    # The vertex should now be in the Graph's vertDict
    self.vertDict[vertexKey1].addNeighbor(self.vertDict[vertexKey2], weight)
  
  # return and array of all of the vertices in the Graph by accessing
  # the keys in the vertexDict
  def getVertices(self):
    return self.vertDict.keys()
  
  # print all of the edges  
  def printVerticesAndEdges(self):
    # loop through all of the vertices associated with this graph
    for v in self.vertDict.values():
        for nbr in v.getConnections():
            print("Vertex: %s, Neighbor: %s, Edge Weight: %s" % (v.id, nbr.getId(), v.neighborsList[nbr]))

  # add an edge both ways with this graph
  def addUndirectedEdge(self, vertexKey1, vertexKey2, weight = 0):
    if vertexKey1 not in self.vertexDict:
      self.vertexDict[vertexKey1] = Vertex(vertexKey1)
    if vertexKey2 not in self.vertexDict:
      self.vertexDict[vertexKey2] = Vertex(vertexKey2)
    self.vertexDict[vertexKey1].addNeighbor(vertexKey2, weight)
    self.vertexDict[vertexKey2].addNeighbor(vertexKey1, weight)