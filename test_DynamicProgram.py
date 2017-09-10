
import unittest
import DynamicProgram

class FiboncciTestCase(unittest.TestCase):
    def setUp(self):
        self.dynProgObj = DynamicProgram.DynamicProgram()
    def test_fib0(self):
        self.assertEqual(self.dynProgObj.fib(0), 0)
    def test_fib1(self):
        self.assertEqual(self.dynProgObj.fib(1), 1)
    def test_fib100(self):
        self.assertEqual(self.dynProgObj.fib(100),354224848179261915075)

if __name__ == '__main__':
    unittest.main()
