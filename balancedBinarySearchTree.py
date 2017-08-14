# tree class is initialized with pointers to a parent tree, value, left child and right child
class Tree:
   def __init__(self, val = None, r = None, l = None, p = None):
        self.val = val              # value in node
        self.r = r                  # right child
        self.l = l                  # left child
        self.p = p                  # parent node

    # insert a new value into the binary search tree
    def insert(self, newVal, parentVal = None):
        if self.val == None:
            self = Tree(newVal)
            self.p = parentVal
            print("The value was added to the tree.")
        elif self.val == newVal:
            print("This value is already in the tree.")
        elif self.val > val:
            insert(self.l, newVal, self.val)
        else:
            insert(self.r, newVal, self.val)
        return
            
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
                    self.val = self.l
                    self.l.insert(self.r)
                else:
                    self.val = self.r
                    self.r.insert(self.l)
            else:
                if self.l != None:
                    self.val = self.l
                else:
                    self.val = self.r
                    
                    
                    
