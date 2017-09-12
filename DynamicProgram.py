# python implementation of dynamic progrmming
# first method include Fibonacci implementation
class DynamicProgram(object):
    def __init__(self):
        self.fib_memo = {}
        self.climb_stairs_memo = {}
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
        
    # basic implementation of dynamic programming by returning the fibonnaci
    # of an 
    def fib(self,n):
        # Check cache
        if n in self.fib_memo:return self.fib_memo[n]
        # Base Cases 0 and 1
        if n <= 0: return 0
        elif n == 1:return 1
        # Backtracking
        result = self.fib(n -1) + self.fib(n-2)
        # Add new result to cache
        self.fib_memo[n] = result
        # return answer
        return result
    
    # basic implementation of dynammic programming
    # return the possible ways to climb n stairs given you can take a maximum of m steps
    def climb_stairs(self, n, m):
        # Search Cache
        """
        if n in self.climb_stairs_memo:
            return self.climb_stairs_memo[n]
        """
        # Base Case
        if n < 0: return 0
        elif n == 1 or n == 0: return 1
        
        # initialize result and counter
        result = 0
        i = 1
        
        # Backtracking
        while i <= m and i <=n:
            result += self.climb_stairs(n-i,m)
            i += 1
        
        # append memo
        #self.climb_stairs_memo[n][m] = result
        
        # return the result
        return result
        
        