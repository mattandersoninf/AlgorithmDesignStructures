class Node:
  def __init__(self, val = None, left=None, right=None):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
  def getValue(self): return self.val
  def getLeftChild(self): return self.left.getValue()
  def getRightChild(self): return self.right.getValue()
  def setValue(self, newVal): self.val = newVal
  def setLeftChild(self, newVal): self.left = Node(newVal)
  def setRightChild(self, newVal): self.right = Node(newVal)
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
  def insert(self, newVal, currNode = None):
    if currNode == None:
      currNode = self.root
    if currNode.val == None:
      currNode.setValue(newVal)
      print(str(newVal)+" was inserted.")
    elif currNode.val == newVal:
      print(str(newVal)+" is already in the tree")
    elif currNode.getValue() > newVal and currNode.left == None:
      currNode.setLeftChild(newVal)
      print(str(newVal)+" was inserted.")
    elif currNode.getValue() > newVal and currNode.left != None:
      self.insert(newVal, currNode.left)
    elif currNode.getValue() < newVal and currNode.right == None:
      currNode.setRightChild(newVal)
      print(str(newVal)+" was inserted.")
    elif currNode.getValue() < newVal and currNode.right != None:
      self.insert(newVal, currNode.right)
      
  # search for whether or not a value is in the tree
  def search(self, searchVal, currNode = None):
    print("search started")
    # start by checking if you're looking at nothing, if so, point to the root of your tree
    if self.root == None:
      return None
    else:
      currNode = self.root
    # if the value of the node that you are currently looking at is equal to the searchVal, return that node
    if currNode.val == searchVal:
      return currNode
    # if the value of the current node is greater than the searchVal and the left child isn't empty, search that node's properties
    elif currNode.getValue() > searchVal and currNode.left != None:
      return self.search(searchVal, currNode.left)
    # if the value of the current node is greater than the searchVal and the right child isn't empty, search that node's properties
    elif currNode.getValue() < searchVal and currNode.right != None:
      return self.search(searchVal, currNode.right)
    # the value must not be in the tree if you've reached this condition
    else:
      return None
  
  # delete a value from the tree
  def delete(self, delVal, currNode = None):
    if self.root != None:
      if self.search(delVal) == None:
        print(str(delVal)+" isn't in the tree")
      else:
        elif self.root == delVal:
          self.root = None
        elif self.root > delVal and self.root.left != None:
          self.delete(delVal, self.root.left)
        elif self.root < delVal and self.root.right != None:
          self.delete(delVal, self.root.right)
    else:
      print("Tree nonexistent.")
      
    
mainTree = Tree()
print(mainTree.root)
mainTree.insert(3)
print(mainTree.search(3).val)
mainTree.delete(3)
print(mainTree.search(3))
"""
mainTree.insert(2)
mainTree.insert(4)
mainTree.insert(1)
print("search 1's value is "+str(mainTree.search(1)))
print("search 2's value is "+str(mainTree.search(2)))
mainTree.insert(5)
mainTree.delete(2)
print("search 2's value is "+str(mainTree.search(2)))
mainTree.insert(1)
mainTree.search(1)
"""
