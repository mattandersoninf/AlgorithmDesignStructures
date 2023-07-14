from heapq import heappop, heappush

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

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.graph}  # Initialize distances with infinity
        distances[start_vertex] = 0

        # Priority queue to store vertices and their distances
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heappop(priority_queue)

            # Ignore outdated entries in the priority queue
            if current_distance > distances[current_vertex]:
                continue

            # Explore neighbors of the current vertex
            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight

                # Update the distance if a shorter path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(priority_queue, (distance, neighbor))

        return distances

        """
        Test Case:
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
print(my_graph)

# Perform Dijkstra's algorithm starting from vertex 'A'
distances = my_graph.dijkstra('A')

# Print the shortest distances from 'A' to all other vertices
print("Shortest distances from 'A':")
for vertex, distance in distances.items():
    print(f"To {vertex}: {distance}")
    
    Output:
    A: B:4, C:2
B: D:5
C: D:8, E:3
D: E:6
E:
Shortest distances from 'A':
To A: 0
To B: 4
To C: 2
To D: 9
To E: 5
    
        
        """