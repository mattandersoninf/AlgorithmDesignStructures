# demonstrate pritority que data structure in python

import collections
# call the graph class to make use of the vertex object
import Graph

class PriorityQueue:
    def __init__(self):
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    
    def append(self, value):
    def pop(self):
    def push(self):
    
def AStar(start, val_to_find):
    if start is None or val_to_find is None: return False
    queue = PriorityQueue()
    queue.append(start)
    while queue:
        current vertex = queue.pop()
        if current_vertex.value == val_to_find: return True
        if not current_vertex.visited:
            current_vertex.visited = True
            for dist, vertex in current_vertex.neighbors:
                vertex.distance = current_vertex.distance + dist
                priority = heuristic(vertex, val_to_find)
                queue.push(priority, vertex)
    return False
            
def djstrika(start, val_to_find):
    if start is None or val_to_find is None: return False
    queue = PriorityQueue()
    queue.append(start)
    while queue:
        if current_vertex.value == val_to_find: return True
        if not current_vertex.visited:
            current_vertex.visited = True
            for dist, vertex in current_vertex.neighbors:
                vertex.distance = current_vetex.distance + dist
                queue.push(vertex.distance, vertex)
    return False
