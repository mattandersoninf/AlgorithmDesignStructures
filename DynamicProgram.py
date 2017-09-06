# python implementation of dynamic progrmming
# first method include Fibonacci implementation
class DynamicProgram(object):
    def __init__(self, memo ={}):
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
        
    def fib(self,n):
        if n in self.memo:
            return self.memo[n]
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        result = self.fib(n -1) + self.fib(n-2)
        self.memo[n] = result
        return result
