# demonstrate pritority que data structure in python

import collections

# min heap under the hood
# still need to get through, don't be intimidated
class PriorityQue:
    def __init__(self):
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    
