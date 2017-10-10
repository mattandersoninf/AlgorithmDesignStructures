
import unittest
import DynamicProgram

class FiboncciTestCase(unittest.TestCase):
    def setUp(self):
        self.dp = DynamicProgram.DynamicProgram()
    
    #
    unittest.skip('currently only need to verify longestSubsequence')
    def test_fib0(self):
        assert self.dp.fib(0) == 0
        assert self.dp.fib(1) == 1
        assert self.dp.fib(100) == 354224848179261915075
    
    #
    unittest.skip('currently only need to verify longestSubsequence')
    def test_climb_stairs(self):
        # permutations = {[1,1,1,1],[1,1,2],[1,2,1],[1,3],[2,1,1],[2,2],[3,1]}
        # answer = len(permutations) = 7
        assert self.dp.climb_stairs(4,3) == 7
        # permutations = {[1,1,1,1,1],[1,1,1,2] ,[1,1,2,1],[1,1,3],[1,2,1,1],[1,2,2],[1,3,1],[2,1,1,1],[2,1,2],[2,2,1],[2,3],[3,1,1],[3,2]}
        # answer = len(permutations) = 13
        assert self.dp.climb_stairs(5,3) == 13
    
    unittest.skip('currently only need to verify longestSubsequence')
    def test_coin_change(self):
        # combinations = {[1,1]}
        # answer = len(combinations) = 1
        assert self.dp.coin_change(2,[5,1]) == 1
        # assert self.dynProgObj.coin_change(2,[1,5]) == 1
        # combinations = {[1,1,1,1,1,1], [1,5]}
        # answer = len(combinations) = 2
        assert self.dp.coin_change(6,[5,1]) == 2
        # combinations = {[1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,5], [1,5,5]}
        # answer = len(combination) = 3
        assert self.dp.coin_change(11,[5,1]) == 3 
        # combinations = {[1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,5], [1,5,5], [1,10]}
        # answer = len(combination) = 4
        assert self.dp.coin_change(11,[10,5,1]) == 4
        
    #unittest.skip()
    def test_longestSubsequence(self):
        assert self.dp.longestSubsequence('','') == 0
        assert self.dp.longestSubsequence('a','a') == 1
        assert self.dp.longestSubsequence('ab','a') == 1
        assert self.dp.longestSubsequence('aba','a') == 1
        assert self.dp.longestSubsequence('ababa','aba') == 3
        assert self.dp.longestSubsequence('abcd','bc') == 2
        assert self.dp.longestSubsequence('abcd','bd') == 2
        


if __name__ == '__main__':
    unittest.main()