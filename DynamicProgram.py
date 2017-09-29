# python implementation of essential dynamic progrmming practices

# import this class to have access to defaultdict
import collections as c

class DynamicProgram(object):
    def __init__(self):
        self.fib_memo = {}
        # nested dictionary, collections.defaultdict works better than a regular nested dictionary
        self.climb_stairs_memo = c.defaultdict(dict)
        self.coin_change_memo = c.defaultdict(dict)
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
        
    # basic implementation of dynamic programming by returning the fibonnaci
    # of an integer n
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
        # Get if you have already done this case, it shoud be
        # stored in the cache under n and m
        if n in self.climb_stairs_memo:
            if m in self.climb_stairs_memo[n]:
                return self.climb_stairs_memo[n][m]

        # Base Case
        # you can't take negative steps so if you loop and n drop below 0
        # return 0
        # there is only 1 way to take 1 step and no steps at all so return 1
        if n < 0: return 0
        elif n == 1 or n == 0: return 1
        
        # initialize result and counter
        # you start by looking at all of the ways you can reach n by taking 1 step and then increase the number of steps
        result = 0
        i = 1
        
        # Backtracking
        # cycle through all of the possible permutations of the ways you can climb
        # n stairs in m allowable steps
        while i <= m and i <=n:
            result += self.climb_stairs(n-i,m)
            i += 1
        
        # append memo that ways if you want to find more solutions, it can recall other
        # other permutations rather than have to recalculate the solution starting from the
        # case every time
        self.climb_stairs_memo[n][m] = result
        
        # return the result
        return result
    
    # return an integer of the number of combinaions you can arrange a coin 
    # array to add up to n before you try using a coin_list as a key,
    # it's not possible because lists are unhashable
    # so it is up the user to please use coins in descending value
    # you can also assume you have an unlimited amount of every coin in coin_array
    # ex: if len(coin_array) == 2, the input should be coin_array = [1,5]    
    def coin_change(self, n, coin_array):
        #  print("start n = "+str(n))
        #  print("start coin_array = "+str(coin_array))
        # check cache to cut down on the runtime, if you've already solved this
        # method for lower "n" values or smaller coin arrays, this function should
        # be able to recognize and call these solutions in the coin_change memo
        if n in self.coin_change_memo:
            if len(coin_array) in self.coin_change_memo[n]:
                return self.coin_change_memo[n][len(coin_array)]
        
        # base cases
        # you can't have negative coin values so return 0 if "n" goes below 0
        # 0 and 1 return 1 because there is only way to organize the values
        # in the coin array (assuming the coin array includes 1) to return
        # these n values 
        if n < 0:
            return 0
        elif n == 1 or n == 0:
            return 1
        
        # result will adjust to the number of arrays returned from backtracking
        # side note: find a way to find the lengths without constructiong all of
        # the arrays for the possible solutions granted the return array have the
        # potential to become very large
        result = 0
        i = 0
        
        # backtracking (the backbone of how this function works)
        # iterate through the values in the coin_array
        while i < len(coin_array) and i <= n:
            result += self.coin_change(n-coin_array[i], coin_array[i:]) # + self.coin_change(n,coin_array[i+1:])
            i += 1
        
        # append to cache
        self.coin_change_memo[n][len(coin_array)] = result
        
        #return result
        return result
