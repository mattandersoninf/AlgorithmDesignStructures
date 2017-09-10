
import unittest
import Graph

# setup the graph test case class by having the setup be initialized to an instance of a Graph object
class GraphTestCase(unittest.TestCase):
    # make a test setup for each testcase function
    # start by making an object adopting the features of the class your testing
    def setUp(self):
        self.graph = Graph.Graph()
    
    # add a test function for each of the functions in the graph
    # this one inparticular is for testing the addVertex method
    def test_addVertex(self):
        self.graph.addVertex(0)
        self.assertTrue(0 in self.graph.vertDict)
        
    # this one in particular is for testing metho addEdge
    def test_addEdge(self):
        self.graph.addEdge(0,1,1)
        self.graph.addEdge(2,3,1,1)
        self.assertIn(1, self.graph.vertDict)
        self.assertIn(2, self.graph.vertDict)
        self.assertIn(3, self.graph.vertDict)
        self.assertIn(1, self.graph.vertDict[0].neighborsList)
        self.assertIn(3, self.graph.vertDict[2].neighborsList)
        self.assertIn(2, self.graph.vertDict[3].neighborsList)
        self.assertEqual(1, self.graph.vertDict[0].neighborsList[1])
        self.assertEqual(1, self.graph.vertDict[2].neighborsList[3])
        self.assertEqual(1, self.graph.vertDict[3].neighborsList[2])
    
    def test_delVertex(self):
        self.graph.delVertex(1)
        self.assertIsNone(self.graph[0])
        self.assertIsNone(self.graph[1].neighborsList[0])
        
    def test_delEdge(self):
        self.graph.delEdge(2,3)
        self.assertIsNone(self.vertDict[2].neighborsList[3])
    
    """
    def test_getVertices(self):
        self.graph.getVertices()
        
    def test_printVertices(self):
        self.graph.printVerticesAndEdges()
    """
              
# main function to run through all of the test function made in the test case
# use the middle arugrument argv=['first-arg-is-ignored'], exit = False because in ipy/ipynb files
# unittest.main looks at sys.argv first so you ignore argv so that unittest.main runs
if __name__ == 'main':
    unittest.main(unittest.main(argv=['first-arg-is-ignored'], exit=False))

