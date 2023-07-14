class IncidenceMatrixGraph:
    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.matrix = [[0] * num_edges for _ in range(num_vertices)]

    def add_edge(self, source, destination, edge_index):
        if 0 <= source < self.num_vertices and 0 <= destination < self.num_vertices and 0 <= edge_index < self.num_edges:
            self.matrix[source][edge_index] = 1
            self.matrix[destination][edge_index] = 1

    def __str__(self):
        return '\n'.join([' '.join([str(x) for x in row]) for row in self.matrix])
