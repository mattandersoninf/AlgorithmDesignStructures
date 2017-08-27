class Node:
  # intialize node class with an intial value, and predefined left child, right child, and parent values
  # the parent is fo rthe sake of the deletion method in the tree class
  def __init__(self, val, left=None, right=None, parent = None):
    # rather than type out each defined attribute of the class, using a dictionary combined with a magic method
    # accomplishes the same task with only a single line
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    # getters and setters for the node attributes
  def getValue(self): return self.val
  def getLeftChild(self): return self.left
  def getRightChild(self): return self.right
  def getParent(self): return self.parent
  def setValue(self, newVal): self.val = newVal
  def setLeftChild(self, newVal): self.left = newVal
  def setRightChild(self, newVal): self.right = newVal
  def setParent(self, newVal): self.parent = newVal
  # return an array of all the attributes that belong to the node
  def getAll(self): return [self.val, self.left, self.right, self.parent]
    
class Tree():
  # intialize a tree with a root value and use the dictionary and magic methods approach to store the attribute
  # could expand further if you wish
  #you should intialize the tree with a Node object
  def __init__(self, root):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
  
  # return the root of the tree
  def getRoot(self):
    return self.root
  
  # set the value of the tre's root
  def setRoot(self, newNode):
    self.root = newNode
  
  # insert a new value into the binary search tree
  def insert(self, root, newNode):
    print("insert started")
    if self.search(root.val) != None:
      if root == None:
        root = newNode
      else:
        if root.val < newNode.val:
          if root.right is None:
            root.right = newNode
            root.right.parent = root
          else: self.insert(root.right, newNode)
        else:
          if root.left is None:
            root.left = newNode
            root.left.parent = root
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
      
  # delete a value from the tree
  def deleteVal(self, root,  delVal):
    leftHold = None
    rightHold = None
    if self.search(delVal) != None:
      while root.val != delVal:
        if delVal < root.val:
          root = root.left
        else:
          root = root.right
      if root.left != None:
        leftHold = root.left
      if root.right != None:
        rightHold = root.right
      if root.parent != None:
        if root.val < root.parent.val:
          root.parent.left = None
        else:
          root.parent.right = None
      else:
        self.root = None
      print(str(delVal)+" was deleted.")
      if leftHold != None:
        self.insert(self.root, leftHold)
      if rightHold !=None:
        self.insert(self.root, rightHold)
    else:
      print(str(delVal)+" is not in the tree.")
  
  # traverse the tree in preorder
  def preorder(self, root):
    if root:
      print(root.val)
      self.preorder(root.left)
      self.preorder(root.right)
  
  # traverse the tree nodes and print their values in order
  def inorder(self, root):
    if root:
      self.inorder(root.left)
      print(root.val)
      self.inorder(root.right)
      
  # traverse the tree nodes in post order    
  def postorder(self, root):
    if root:
      self.postorder(root.left)
      self.postorder(root.right)
      print(root.val)

# intial testing to prove insert, search, and delete functions work
mainTree = Tree(Node(5))
print(mainTree.root)
print(mainTree.search(5))
mainTree.insert(mainTree.root, Node(3))
print(mainTree.search(3))
mainTree.insert(mainTree.root, Node(4))
print(str(mainTree.search(4))+": node for 4")
mainTree.insert(mainTree.root, Node(1))
print(str(mainTree.search(1))+": node for 1")
mainTree.deleteVal(mainTree.root, 3)
print(mainTree.search(3))
print(mainTree.search(4))
print(mainTree.search(1))
mainTree.insert(mainTree.root, Node(7))
print(str(mainTree.root.left.val)+": if done properly, this should be 1.")
print(str(mainTree.root.left.right.val)+": if done properly, this should be 4.")
#mainTree.preorder(mainTree.root)
#mainTree.inorder(mainTree.root)
#mainTree.postorder(mainTree.root)


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
