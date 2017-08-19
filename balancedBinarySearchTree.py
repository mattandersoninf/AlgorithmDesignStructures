# tree class is initialized with pointers to a parent tree, value, left child and right child
class Node:
   def __init__(self, val, left=None, right=None):
   self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
   def getValue(self):
      return self.val
   def getLeftChild(self):
      return self.left
   def getRightChild(self):
      return self.right

class Tree():

    # insert a new value into the binary search tree
    def insert(self, newVal):
        if self.
            
    def search(self, val):
        if self.val == None:
            print("The value " + str(val) + " is not in the tree.")
        elif self.val == val:
            print("The value " + str(val) + " is in this tree.")
            if self.p != None:
                print("The parent value is " + str(self.p))
            if self.l != None:
                print("The left child is " + str(self.l))
            if self.r != None:
                print("The right child is " + str(self.r))
        elif self.val > val:
            insert(self.l, newVal, self.val)
        else:
            insert(self.r, newVal, self.val)
        return
        
    # delete node from tree
    def delete(self, val):
        if self.val == None:
            print("The value " + str(val) + " is not in the tree.")
        elif self.val == val:
            if self.l == None and self.r == None:
                self == None
            elif self.l != None and self.r != None:
                if self.p < self.val:
                    temp = self.r
                    self = self.l
                    self.insert(temp)
                else:
                    temp = self.l
                    self = self.r
                    self.insert(temp)
            else:
                if self.l != None:
                    self.val = self.l
                else:
                    self.val = self.r
                    
                    
