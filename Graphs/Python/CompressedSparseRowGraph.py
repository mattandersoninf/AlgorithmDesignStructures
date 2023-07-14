class CompressedSparseRowGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.row_ptr = [0] * (num_vertices + 1)
        self.col_indices = []
        self.weights = []

    def add_edge(self, source, destination, weight):
        self.col_indices.append(destination)
        self.weights.append(weight)
        self.row_ptr[source + 1] += 1

    def __str__(self):
        return f"row_ptr: {self.row_ptr}\ncol_indices: {self.col_indices}\nweights: {self.weights}"
