
import unittest
import DynamicProgram

class FiboncciTestCase(unittest.TestCase):
    def setUp(self):
        self.dynProgObj = DynamicProgram.DynamicProgram()
    
    def test_fib0(self):
        assert self.dynProgObj.fib(0) == 0
    def test_fib1(self):
        assert self.dynProgObj.fib(1) == 1
    def test_fib100(self):
        assert self.dynProgObj.fib(100) == 354224848179261915075
    def test_climb_stairs_4_3(self):
        # permutations = {[1,1,1,1],[1,1,2],[1,2,1],[1,3],[2,1,1],[2,2],[3,1]}
        # answer = len(permutations) = 7
        assert self.dynProgObj.climb_stairs(4,3) == 7
        # permutations = {[1,1,1,1,1],[1,1,1,2],[1,1,2,1],[1,1,3],[1,2,1,1],[1,2,2],[1,3,1],[2,1,1,1],[2,1,2],[2,2,1],[2,3],[3,1,1],[3,2]}
        # answer = len(permutations) = 13
    def test_climbs_stairs_5_3(self):
        assert self.dynProgObj.climb_stairs(5,3) == 13
    
    
    def test_coin_change(self):
        # combinations = {[1,1]}
        # answer = len(combinations) = 1
        assert self.dynProgObj.coin_change(2,[5,1]) == 1
        # assert self.dynProgObj.coin_change(2,[1,5]) == 1
        # combinations = {[1,1,1,1,1,1], [1,5]}
        # answer = len(combinations) = 2
        assert self.dynProgObj.coin_change(6,[5,1]) == 2
        # combinations = {[1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,5], [1,5,5]}
        # answer = len(combination) = 3
        assert self.dynProgObj.coin_change(11,[5,1]) == 3 
        # combinations = {[1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,5], [1,5,5], [1,10]}
        # answer = len(combination) = 4
        assert self.dynProgObj.coin_change(11,[10,5,1]) == 4


if __name__ == '__main__':
    unittest.main()