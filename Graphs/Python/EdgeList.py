class EdgeListGraph:
    def __init__(self):
        self.edges = []

    def add_edge(self, source, destination):
        self.edges.append((source, destination))

    def __str__(self):
        return '\n'.join([f"({source}, {destination})" for source, destination in self.edges])
