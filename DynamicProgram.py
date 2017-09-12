# python implementation of dynamic progrmming
# first method include Fibonacci implementation
class DynamicProgram(object):
    def __init__(self, memo ={}):
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
        
    # basic implementation of dynamic programming by returning the fibonnaci
    # of an 
    def fib(self,n):
        # typeerror for non integers
        if type(n) != 'int':
            raise TypeError("You need to put in an integer.")
        # Check cache
        if n in self.memo:return self.memo[n]
        # Base Cases 0 and 1
        if n <= 0: return 0
        elif n == 1:return 1
        # Backtracking
        result = self.fib(n -1) + self.fib(n-2)
        # Add new result to cache
        self.memo[n] = result
        # return answer
        return result
