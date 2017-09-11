# class structure for vertex, utilizes the value parameter as the key
# and an array of neighbor nodes
# Set up the dictionary so that the Vertex will have a key parameter and 
# a dictionary of neighbors with the neighbor values as the keys
# and the weight to that neighbor as the associated value

import collections

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
    def getConnections(self):return list(self.neighborsList.keys())
    
    # return the vertex's object id
    def getId(self):return self.id
      
    # return the weight associated with a specific neighbor to this vertex    
    def getWeight(self,nbr):return self.neighborsList[nbr]
      
    # set the visited parameter to true
    def setVisitTrue(self):self.visited = True
    
    # set the visited parameter to false
    def setVisitFalse(self):self.visited = False
    
    # delete a neighbor value and it's weight in the neighborsList dictionary
    def delNeighbor(self,value): del self.neighborsList[value]

# class structure for graph  
class Graph(object):
    # utilize the dictionary to keep track of all the parameters within the Graph
    # eliminates the need for self.parameter = parameter for every parameter in the
    # initializer in case you want to add more parameters
    def __init__(self, vertDict = {}):
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
  
    # add a vertex object to vertDict in the Graph class 
    def addVertex(self, v):
        # you can't add values to a key in a dictionary if it already exists, so track
        # the Exception
        if v in self.vertDict:
            raise Exception(str(v) + " is already in this Graph.")
        # given a key value, make a new vertex and treat that value as the key to connect to
        # that value
        newVertex = Vertex(v)
        self.vertDict[v] = newVertex

    # Add an edge to the Graph class, inputs should be 2 integer values
    # A weight can be specified to the path otherwise the weight will be 
    # set to 0  
    def addEdge(self, v1, v2, weight1 = 0, weight2 = None):
        # If the specified vertex values aren't in the Graph already
        # add them to the vertDict
        if v1 not in self.vertDict: self.addVertex(v1)
        if v2 not in self.vertDict: self.addVertex(v2)
        # check if there was a second weight which will make this path undirected
        if weight2 == None:
            self.vertDict[v1].addNeighbor(self.vertDict[v2], weight1)
        else:
            self.vertDict[v1].addNeighbor(self.vertDict[v2], weight1)
            self.vertDict[v2].addNeighbor(self.vertDict[v1], weight2)
            
    # delete vertx value from the graph's vertex dictionary
    def delVertex(self, value):
        # delete this value from all of the vertices' neihborsLists
        for v in self.vertDict:
            if self.vertDict[value] in self.vertDict[v].neighborsList:
                self.vertDict[v].delNeighbor(self.vertDict[value])
        # delete the specified key value from the vertex dictionary of the graph
        del self.vertDict[value]
        
    # delete an edge from the Graph by removing that vertex object from the
    # neighbor list
    def delEdge(self, vertexKey1, vertexKey2):
        # delete the neighbor
        if self.vertDict[vertexKey2] in self.vertDict[vertexKey1].neighborsList:
            self.vertDict[vertexKey1].delNeighbor(self.vertDict[vertexKey2])
        
  
    # return and array of all of the vertices in the Graph by accessing
    # the keys in the vertDict
    def getVertices(self): return self.vertDict.keys()
  
    # print all of the edges  
    def printVerticesAndEdges(self):
        # loop through all of the vertices associated with this graph
        for v in self.vertDict.values():
            for nbr in v.getConnections(): print("Vertex: %s, Neighbor: %s, Edge Weight: %s" % (v.id, nbr.getId(), v.neighborsList[nbr]))

#----------------------------------------------------------------------------------------------------------------------------------------
    # Unweighted Traversals
    #
    def bfs(self, start, val):
        #
        if start is None or val is None: return False
        queue = collections.deque([])
        queue.append(start)
        while queue:
            current_vertex = queue.pop()
            if current_vertex.id == val:
                return True
            if not current_vertex.visited:
                current_vertex.setVistTrue()
                for vertex in current_vertex.neighborsList:
                    queue.appendleft()
        return False
    
    #                
    def dfs(self, vertex, val):
        #
        if not vertex.visited:
            vertex.setVisitedTrue()
            if vertex.id == val:
                return True
            for neighbor_vertex in vertex.neighborsList:
                is_found = self.dfs(neighbor_vertex, val)
                if is_found: return True
        return False