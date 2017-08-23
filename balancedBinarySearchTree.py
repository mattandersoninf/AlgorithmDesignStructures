class Node:
  def __init__(self, val, left=None, right=None):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
  def getValue(self): return self.val
  def getLeftChild(self): return self.left.getValue()
  def getRightChild(self): return self.right.getValue()
  def setValue(self, newVal): self.val = newVal
  def setLeftChild(self, newVal): self.left = newVal
  def setRightChild(self, newVal): self.right = newVal
  # 
  def getAll(self): return [self.getValue(), self.getLeftChild(), self.getRightChild()]
    
class Tree():
  def __init__(self, root = Node(None)):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
  
  def getRoot(self):
    return self.root
  
  def setRoot(self, newNode):
    self.root = newNode
  
  # insert a new value into the binary search tree
  def insertVal(self, newVal):
    if self.root.getValue() == None:
      self.root.setValue(newVal)
      print("root was set to "+str(newVal))
    elif self.root.getValue() > newVal and self.root.left == None:
      print("started insertNode on left side")
      self.root.left = Node(newVal)
    elif self.root.getValue() > newVal and self.root.left != None:
      self.insertNode(newVal, self.root.left)
    elif self.root.getValue() < newVal and self.root.right == None:
      self.root.right = Node(newVal)
    elif self.root.getValue() < newVal and self.root.right != None:
      self.insertNode(newVal, self.root.left)
      
      
  def insertNode(self, newVal, currNode):
    if currNode  == None:
      print(currNode)
      print("Node was inserted")
      currNode = Node(newVal)
      print(currNode)
    elif currNode.getValue() > newVal:
      print("considering left insert")
      self.insertNode(newVal, currNode.left)
    else:
      print("considering right insert")
      self.insertNode(newVal, currNode.right)
  
  # search for whether or not a value is in the tree
  def searchVal(self, searchVal):
    if self.root.getValue() == searchVal:
      print(str(searchVal), " is the root of the tree")
    elif self.root.getValue() > searchVal and self.root.left != None:
      self.searchNode(searchVal, self.root.left)
    elif self.root.getValue() < searchVal and self.root.right != None:
      self.searchNode(searchVal, self.root.right)
    else:
      print(str(searchVal)+ " is not in the tree.")
      
  def searchNode(self, searchVal, currNode):
    if currNode.getValue() == searchVal:
      print(str(searchVal)+" is in the tree.")
    elif currNode.getValue() > searchVal and currNode.left != None: self.searchNode(searchVal, currNode.left)
    elif currNode.getValue() < searchVal and currNode.right != None: self.searchNode(searchVal, currNode.right)
    else:
      print(str(searchVal)+ " is not in the tree.")
      
  """
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
  """  
    
mainTree = Tree()
print(mainTree.root.getValue())
mainTree.insertVal(3)
print(mainTree.getRoot().getValue())
mainTree.insertVal(2)
print("left node is "+str(mainTree.root.getLeftChild()))
mainTree.insertVal(4)
print("right node is "+str(mainTree.root.getRightChild()))
print(mainTree.searchVal(2))
print(mainTree.searchVal(1))
print(mainTree.insertVal(1))
print(mainTree.searchVal(1))

"""
mainTree.insert(5)
mainTree.delete(2)
mainTree.search(2)
mainTree.insert(1)
mainTree.search(1)
"""
