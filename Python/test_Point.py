import unittest
from Point import Point

class TestPoint(unittest.TestCase):  

    def test_coordinates1(self):
        testPoint = Point(2,2)
        self.assertEqual(testPoint.coordinates, (2,2),"Should be (2,2)")
        
    def test_coordinates2(self):
        testPoint = Point(-3,1)
        self.assertEqual(testPoint.coordinates,(-3,1),"Should be (-3,1)")

    def test_coordinates3(self):
        testPoint = Point(4,5)
        self.assertEqual(testPoint.coordinates,(4,5),"Should be (4,5)")

    def test_moveTo1(self):
        testPoint = Point(2,2)
        testPoint.moveTo(3,3)
        self.assertEqual(testPoint.coordinates,(3,3),"Should be (3,3)")

    
    def test_moveTo2(self):
        testPoint = Point(1,1)
        testPoint.moveTo(-1,-1)
        self.assertEqual(testPoint.coordinates,(-1,-1),"Should be (-1,-1)")

    
    def test_moveTo3(self):
        testPoint = Point(2,-3)
        testPoint.moveTo(-4,1)
        self.assertEqual(testPoint.coordinates,(-4,1),"Should be (-4,1)")


    def test_distanceTo1(self):
        testPoint = Point(2,2)
        resultDistance = testPoint.distanceTo(5,6)
        self.assertEqual(resultDistance,5.0,"Should be 5.0")


    def test_distanceTo2(self):
        testPoint = Point(-6,8)
        resultDistance = testPoint.distanceTo(0,0)
        self.assertEqual(resultDistance,10.0,"Should be 10.0")


    def test_distanceTo3(self):
        testPoint = Point(-10,2)
        resultDistance = testPoint.distanceTo(2,-3)
        self.assertEqual(resultDistance,13.0,"Should be 13.0")

    def test_distanceTo4(self):
        testPoint = Point(-10,2)
        resultDistance = testPoint.distanceTo(2,-3)
        # this should fail just to prove that the other functions work as intended
        self.assertEqual(resultDistance,12,"Should be 13.0")



if __name__ == "__main__":
    unittest.main()