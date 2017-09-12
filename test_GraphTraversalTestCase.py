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
    #
    def test_0bfs(self):
        # the test graph has vertices of values 0 - 9
        for i in range(10): self.graph.addVertex(i)
        # the vertex 0 gets connected to vertices 1-5 with a weight of 1
        for i in range(1,6):self.graph.addEdge(0,i,1)
        # the vertex 1 gets connected to vertices 2-4 with a weight of 1
        for i in range(2,5):self.graph.addEdge(1,i,1)
        # the vertex 2 gets connected to vertices 5-9 with a weight of 1
        for i in range(5,10):self.graph.addEdge(2,i,1)
        # create an edge from 1 to 0
        self.graph.addEdge(1,0,1)
        self.assertTrue(self.graph.bfs(self.graph.vertDict[1],0))
        self.assertTrue(self.graph.bfs(self.graph.vertDict[0],2))
    
    def test_1dfs(self):
        self.assertTrue(self.graph.dfs(self.graph.vertDict[0],2))
       
if __name__ == '__main__':
    unittest.main()