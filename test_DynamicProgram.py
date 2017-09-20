
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
        # combinations = {[1,1]}
        # answer = len(combinations) = 1
        print("coin_change(2,[1,5])",self.dynProgObj.coin_change(2,[1,5]))
        # assert self.dynProgObj.coin_change(2,[1,5]) == 1
        # combinations = {[1,1,1,1,1,1], [1,5]}
        # answer = len(combinations) = 2
        print("coin_change(6,[5,1])",self.dynProgObj.coin_change(6,[5,1]))
        # combinations = {[1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,5], [1,5,5]}
        # answer = len(combination) = 3
        print("coin_change(11,[1,5])",self.dynProgObj.coin_change(11,[1,5]))
        # combinations = {[1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,5], [1,5,5], [1,10]}
        # answer = len(combination) = 4
        #assert self.dynProgObj.coin_change(11,[1,5,10]) == 4


if __name__ == '__main__':
    unittest.main()