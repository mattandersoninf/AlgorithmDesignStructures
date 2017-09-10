
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
    def test_0addVertex(self):
        print("testing addVertex")
        self.graph.addVertex(0)
        print(self.graph.vertDict.keys())
        self.assertIn(0, self.graph.vertDict)
    
    # this one in particular is for testing method addEdge
    def test_1addEdge(self):
        print("testing addEdge")
        self.graph.addEdge(0,1,1)
        print(self.graph.vertDict.keys())
        self.graph.addEdge(2,3,1,1)
        print(self.graph.vertDict.keys())
        self.assertIn(1, self.graph.vertDict)
        self.assertIn(2, self.graph.vertDict)
        self.assertIn(3, self.graph.vertDict)
        self.assertIn(self.graph.vertDict[1], self.graph.vertDict[0].neighborsList)
        self.assertIn(self.graph.vertDict[3], self.graph.vertDict[2].neighborsList)
        self.assertIn(self.graph.vertDict[2], self.graph.vertDict[3].neighborsList)
        self.assertEqual(1, self.graph.vertDict[0].neighborsList[self.graph.vertDict[1]])
        self.assertEqual(1, self.graph.vertDict[2].neighborsList[self.graph.vertDict[3]])
        self.assertEqual(1, self.graph.vertDict[3].neighborsList[self.graph.vertDict[2]])
    
    def test_2delVertex(self):
        print("testing delVertex")
        self.graph.delVertex(1)
        print(self.graph.vertDict.keys())
        self.assertNotIn(1, self.graph.vertDict)
    
    def test_3delEdge(self):
        print("testing delEdge")
        self.graph.delEdge(2,3)
        print(self.graph.vertDict.keys())
        self.assertNotIn(self.graph.vertDict[3], self.graph.vertDict[2].neighborsList)
        
    def test_4getVertices(self):
        print("testing getVertices")
        print(self.graph.getVertices())
    
    def test_5printVertices(self):
        self.graph.printVerticesAndEdges()
    
    
              
# main function to run through all of the test function made in the test case
# use the middle arugrument argv=['first-arg-is-ignored'], exit = False because in ipy/ipynb files
# unittest.main looks at sys.argv first so you ignore argv so that unittest.main runs
if __name__ == '__main__':
    unittest.main()
