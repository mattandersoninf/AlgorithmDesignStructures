class Node:
  def __init__(self, val, left=None, right=None):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
  def getValue(self): self.val
  def getLeftChild(self): self.left
  def getRightChild(self): self.right
  def setValue(self, newValue): self.val = newValue
  def setLeftChild(self, newValue): self.left = newValue
  def setRightChild(self, newValue): self.right = newValue
    
class Tree():
  def __init__(self, root):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
  def getRoot(self):
    return self.root
  
  """
  # insert a new value into the binary search tree
  def insertVal(self, newVal, currNode = None):
    if self.root == None:
      self.root = Node(newVal)
      return
    elif currNode.:
      
      
  def insertNode(self, newNode):
    temp = self.root
    if temp.val  > newNode.getValue() and newNode.left == None:
      print("check left insert")
    elif int(self.root()) < newVal and self.root == None:
      print("check right insert")
      self.right = Tree(newVal)
    elif int(self.getValue()) > newVal and int(self.getLeftChild()) != None:
      print("check pass left")
      self.left.insert(newVal)
    else:
      print("check pass right")
      self.right.insert(newVal)
  """    
  # search for whether or not a value is in the tree
  def search(self, searchVal):
    if self.val == searchVal:
      return str(searchVal), " is in the tree."
    elif searchVal < self.val and self.left != None:
      return self.left.search(searchVal)
    elif searchVal > self.val and self.right != None:
      return self.right.search(searchVal)
    else:
      return str(searchVal), " is not in the tree."
  
  # delete a value from the tree
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
print(mainTree.getRoot())
mainTree.insertVal(2)
mainTree.insertVal(4)
print(mainTree.search(2))
"""
mainTree.insert(5)
mainTree.delete(2)
mainTree.search(2)
mainTree.insert(1)
mainTree.search(1)
"""
