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
  def __init__(self, root, nil = Node()):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    
  def getRoot(self):
    return self.root
  
  def setRoot(self, newNode):
    self.root = newNode
  
  # insert a new value into the binary search tree
  def insert(self, root, newNode):
    if self.search(root.val) != None:
      if root == None:
        root = newNode
      else:
        if root.val < newNode.val:
          if root.right is None: root.right = newNode
          else: self.insert(root.right, newNode)
        else:
          if root.left is None: root.left = newNode
          else: self.insert(root.left, newNode)
    else:
      print(str(newNode.val) + " is already in the tree.")
    
    
   
  # search for whether or not a value is in the tree
  def search(self, searchVal, currNode = None):
    # start by checking if you're looking at nothing, if so, point to the root of your tree
    if currNode == None:
      currNode = self.root
    if currNode == None:
      return None
    else:
      # if the value of the node that you are currently looking at is equal to the searchVal, return that node
      if currNode.val == searchVal:
        return currNode
      elif currNode.val == None:
        return None
      # if the value of the current node is greater than the searchVal and the left child isn't empty, search that node's properties
      elif currNode.val > searchVal and currNode.left != None:
        return self.search(searchVal, currNode.left)
      # if the value of the current node is greater than the searchVal and the right child isn't empty, search that node's properties
      elif currNode.val < searchVal and currNode.right != None:
        return self.search(searchVal, currNode.right)
      # the value must not be in the tree if you've reached this condition
      
  """
  # delete a value from the tree
  def delete(self, root,  delNode):
    if self.search(delNode.val) != None:
      
    else:
      print(str(delNode.val)+" is not in the tree.")
  """   
    
mainTree = Tree(Node(3))
print(mainTree.root)
print(str(mainTree.search(3)) +" means 3 init works.")
mainTree.insert(mainTree.root, Node(2))
print(str(mainTree.search(2))+" means 2 insert works")
mainTree.insert(mainTree.root, Node(1))
print(str(mainTree.search(1))+" means 1 insert works")
print(str(mainTree.search(4))+" means 4 insert works")
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
