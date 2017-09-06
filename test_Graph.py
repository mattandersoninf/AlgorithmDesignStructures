# 
import unittest
import Graph

class GraphTestCase(unittest.TestCase):
    def setUp(self):
        # make a base test Graph with a size of 9x9 at the beginning
        # still need to figure out how to make it expandable
        self.graphObj = Graph(9)
    
    # testing adding a vertex to the vertDict parameter in the Graph class
    def test_addVertex(self):
        self.graphObj.addVertex(0,1,5)
        self.assertEqual(self.graphObj[0])
        

"""
mainGraph = Graph(9)
for i in range(len(mainGraph.matrix)):
  mainGraph.addVertex(i)
mainGraph.addEdge(0,1,5)
mainGraph.addEdge(5,4,6)
mainGraph.addEdge(5,6,4)
mainGraph.addEdge(8,5,5)
print(mainGraph.getVertices())
mainGraph.printVertDict()
mainGraph.printMatrix()
"""