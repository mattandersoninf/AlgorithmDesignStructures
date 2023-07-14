class AdjacencyMatrixGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, source, destination):
        if 0 <= source < self.num_vertices and 0 <= destination < self.num_vertices:
            self.matrix[source][destination] = 1
            self.matrix[destination][source] = 1

    def __str__(self):
        return '\n'.join([' '.join([str(x) for x in row]) for row in self.matrix])
