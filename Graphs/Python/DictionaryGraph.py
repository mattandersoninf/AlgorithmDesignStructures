class DictionaryGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination):
        if source in self.graph and destination in self.graph:
            self.graph[source].append(destination)
            self.graph[destination].append(source)

    def __str__(self):
        return '\n'.join([f"{vertex}: " + ', '.join(str(neighbor) for neighbor in neighbors) for vertex, neighbors in self.graph.items()])
