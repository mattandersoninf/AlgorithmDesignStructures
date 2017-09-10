# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:06:31 2017

@author: mattanderson
"""

import unittest
import Graph

# testcase class for graph traversal functions
class GraphTraversalTestCase(unittest.TestCase):
    # 
    def setUp(self):
        self.graph = Graph.Graph()
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    
    #
    def test_bfs(self):
        