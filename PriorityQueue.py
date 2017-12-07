# demonstrate pritority que data structure in python

import collections
# call the graph class to make use of the vertex object
import Graph

class PriorityQueue:
    def __init__(self):
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    
    
