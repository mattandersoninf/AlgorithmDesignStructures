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
        if nbr in self.neighborsList:
            print(str(nbr)+" is already in the neighborsList of vertex " + str(self.id))
            return
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
            print(str(v.id) + " is already in this Graph.")
            return
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
        if weight2 == None: self.vertDict[v1].addNeighbor(self.vertDict[v2], weight1)
        else:
            self.vertDict[v1].addNeighbor(self.vertDict[v2], weight1)
            self.vertDict[v2].addNeighbor(self.vertDict[v1], weight2)
            
    # delete vertx value from the graph's vertex dictionary
    def delVertex(self, value):
        # delete this value from all of the vertices' neihborsLists
        if value in self.vertDict:
            for v in self.vertDict:
                if self.vertDict[value] in self.vertDict[v].neighborsList:
                    self.vertDict[v].delNeighbor(self.vertDict[value])
            # delete the specified key value from the vertex dictionary of the graph
            del self.vertDict[value]
        else: print(str(value)+" is not in the Graph.")
        
    # delete an edge from the Graph by removing that vertex object from the
    # neighbor list
    def delEdge(self, vertexKey1, vertexKey2):
        # delete the neighbor
        if self.vertDict[vertexKey2] in self.vertDict[vertexKey1].neighborsList:
            self.vertDict[vertexKey1].delNeighbor(self.vertDict[vertexKey2])
        else: print(str(vertexKey2)+" is not a neighbor of "+str(vertexKey1))
  
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
    # breadth first search
    # visual representation: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/
    # search algorithm for checking all of the neighbors of the current node before traversing
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
                current_vertex.setVisitTrue()
                for vertex in current_vertex.neighborsList:
                    queue.appendleft(vertex)
        return False
    
    # depth first search
    # visual representation: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/
    # search algorithm for travsing paths until you have no neighbors then return to the original node 
    # and try down another path
    def dfs(self, vertex, val):
        #
        if not vertex.visited:
            vertex.setVisitTrue()
            if vertex.id == val:
                return True
            for neighbor_vertex in vertex.neighborsList:
                is_found = self.dfs(neighbor_vertex, val)
                if is_found: return True
        return False
    
    def searchCleanup(self):
        for vertex in self.vertDict.values():
            vertex.setVisitFalse()
    
    # def djstrika(self, vertex, value):
    
"""
    class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.graph and destination in self.graph:
            self.graph[source][destination] = weight

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex].items():
                edges.append((vertex, neighbor, weight))
        return edges

    def __str__(self):
        graph_str = ""
        for vertex in self.graph:
            graph_str += f"{vertex}: "
            graph_str += ", ".join(f"{neighbor}:{weight}" for neighbor, weight in self.graph[vertex].items())
            graph_str += "\n"
        return graph_str

    def depth_first_search(self, start_vertex):
        visited = set()  # Set to keep track of visited vertices
        self._dfs_helper(start_vertex, visited)

    def _dfs_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")  # Process the vertex
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

    def breadth_first_search(self, start_vertex):
        visited = set()  # Set to keep track of visited vertices
        queue = [start_vertex]  # Queue for BFS traversal
        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")  # Process the vertex
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.graph}  # Initialize distances with infinity
        distances[start_vertex] = 0

        visited = set()  # Set to keep track of visited vertices

        while len(visited) < len(self.graph):
            # Find the vertex with the minimum distance among unvisited vertices
            min_distance = float('inf')
            min_vertex = None
            for vertex in self.graph:
                if vertex not in visited and distances[vertex] < min_distance:
                    min_distance = distances[vertex]
                    min_vertex = vertex

            visited.add(min_vertex)  # Mark the vertex as visited

            # Update the distances of neighboring vertices
            for neighbor, weight in self.graph[min_vertex].items():
                distance = distances[min_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances
        
""" 
        