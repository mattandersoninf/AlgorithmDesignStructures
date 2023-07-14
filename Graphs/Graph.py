class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store the graph

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}  # Create an empty dictionary as the value for the new vertex

    def add_edge(self, source, destination, weight):
        if source in self.graph and destination in self.graph:
            self.graph[source][destination] = weight  # Add the destination and weight to the source's dictionary of neighbors

    def get_vertices(self):
        return list(self.graph.keys())  # Return a list of all vertices in the graph

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex].items():
                edges.append((vertex, neighbor, weight))  # Append each edge as a tuple (source, destination, weight) to the edges list
        return edges

    def __str__(self):
        graph_str = ""
        for vertex in self.graph:
            graph_str += f"{vertex}: "
            graph_str += ", ".join(f"{neighbor}:{weight}" for neighbor, weight in self.graph[vertex].items())  # Concatenate the neighbors and their weights of each vertex
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
                self._dfs_helper(neighbor, visited)  # Recursively call the helper function for unvisited neighbors

    def breadth_first_search(self, start_vertex):
        visited = set()  # Set to keep track of visited vertices
        queue = [start_vertex]  # Queue for BFS traversal
        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")  # Process the vertex
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)  # Enqueue unvisited neighbors
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
# Create a graph object
my_graph = Graph()

# Add vertices
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.add_vertex('E')

# Add edges with weights
my_graph.add_edge('A', 'B', 4)
my_graph.add_edge('A', 'C', 2)
my_graph.add_edge('B', 'D', 5)
my_graph.add_edge('C', 'D', 8)
my_graph.add_edge('C', 'E', 3)
my_graph.add_edge('D', 'E', 6)

# Print the graph
print("Graph:")
print(my_graph)

# Get vertices
vertices = my_graph.get_vertices()
print("Vertices:", vertices)

# Get edges
edges = my_graph.get_edges()
print("Edges:")
for edge in edges:
    print(edge)

# Perform depth-first search starting from vertex 'A'
print("DFS traversal:")
my_graph.depth_first_search('A')
print()

# Perform breadth-first search starting from vertex 'A'
print("BFS traversal:")
my_graph.breadth_first_search('A')
print()

# Perform Dijkstra's algorithm starting from vertex 'A'
distances = my_graph.dijkstra('A')
print("Shortest distances from 'A':")
for vertex, distance in distances.items():
    print(f"To {vertex}: {distance}")
"""


"""
1. Adjacency Matrix: An adjacency matrix represents a graph using a 2D matrix. The rows and columns of the matrix correspond to vertices, and the matrix elements indicate the presence or absence of edges between vertices.

2. Adjacency List: An adjacency list represents a graph using a collection of lists or arrays. Each vertex has a list of its neighboring vertices, storing the edges.

3. Edge List: An edge list is a simple representation of a graph that lists all the edges explicitly. Each edge is typically represented as a pair of vertices.

4. Incidence Matrix: An incidence matrix represents a graph using a matrix where the rows represent vertices and the columns represent edges. The matrix elements indicate the presence or absence of edges between vertices and edges.

5. Hash Table or Dictionary: A hash table or dictionary can be used to represent a graph where the keys are vertices, and the values are lists of adjacent vertices.

6. Compressed Sparse Row (CSR): The CSR format is used to represent a sparse graph efficiently by storing the edges and vertices in arrays. It combines the benefits of both the adjacency list and adjacency matrix representations.

These different graph data structures have varying advantages and disadvantages in terms of storage efficiency, ease of traversal, and memory requirements. The choice of which data structure to use depends on the specific requirements of the application and the characteristics of the graph being represented.
"""