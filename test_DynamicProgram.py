
import unittest
import DynamicProgram

class FiboncciTestCase(unittest.TestCase):
    def setUp(self):
        self.dynProgObj = DynamicProgram.DynamicProgram()
    """
    def test_fib0(self):
        self.assertEqual(self.dynProgObj.fib(0), 0)
    def test_fib1(self):
        self.assertEqual(self.dynProgObj.fib(1), 1)
    def test_fib100(self):
        self.assertEqual(self.dynProgObj.fib(100),354224848179261915075)
    def test_climb_stairs3(self):
        print(self.dynProgObj.climb_stairs(4,3))
        print(self.dynProgObj.climb_stairs(7,3))
    """
    def test_coin_change(self):
        print(self.dynProgObj.coin_change(2,[1,5]))
        print(self.dynProgObj.coin_change(6,[1,5]))
        print(self.dynProgObj.coin_change(7,[1,5]))
        print(self.dynProgObj.coin_change(11,[1,5]))

if __name__ == '__main__':
    unittest.main()
