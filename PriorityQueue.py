# demonstrate pritority que data structure in python

import collections
import Graph

class PriorityQueue:
    def __init__(self):
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    
    
