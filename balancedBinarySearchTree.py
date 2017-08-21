# make sure that tree class inherits from node
class Node:
  def __init__(self, val, left=None, right=None):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
  def getValue(self):
    return self.val
  def getLeftChild(self):
    return self.left.getValue()
  def getRightChild(self):
    return self.right.getValue()
    
class Tree(Node):
  def __init__(self):
    super(Tree, self).__init__(self)
  # insert a new value into the binary search tree
  @classmethod
  def insert(self, newVal):
    if self == None:
      self = Node(newVal)
    else:
      print(self.getValue(self))
      print(self.getLeftChild(self))
      print(self.getRightChild(self))
      if self.getValue(self) > newVal and self.getLeftChild(self) == None:
        self.left = Tree(newVal)
      elif self.getValue(self) < newVal and self.getRightChild(self) == None:
        self.right = Tree(newVal)
      elif self.getValue(self) > newVal and self.getLeftChild(self) != None:
        self.left.insert(newVal)
      else:
        self.right.insert(newVal)
  
  # search for whether or not a value is in the tree
  @classmethod
  def search(self, searchVal):
    if self.val == searchVal:
      return str(searchVal), " is in the tree."
    elif searchVal < self.val and self.left != None:
      return self.left.search(searchVal)
    elif searchVal > self.val and self.right != None:
      return right.search(searchVal)
    else:
      return str(searchVal), " is not in the tree."
  
  # delete a value from the tree
  @classmethod
  def delete(self, delVal):
    if self.val == delVal and self.left == None and self.right == None:
      self = None
    elif self.val == delVal and self.left != None and self.right == None:
      self = self.left
    elif self.val == delVal and self.left == None and self.right != None:
      self = self.right
    elif self.val == delVal and self.left != None and self.right != None:
      temp = self.right
      self = self.left
      self.insert(temp)
    return
    
mainTree = Tree(3)
print(mainTree.getValue())
mainTree.insert(2)
mainTree.insert(4)
print(mainTree.getRightChild())
print(mainTree.getLeftChild())
mainTree.insert(5)
mainTree.search(2)
mainTree.delete(2)
mainTree.search(2)
mainTree.insert(1)
mainTree.search(1)
                    
