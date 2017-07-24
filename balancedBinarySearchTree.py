# remember to incoporate
# self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
class Node(object):
  # initialize a node with key and a a set velue
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.right = right
    self.left =  left
  
  # get right child of node
  def right(self):
    return self.right
  
  # get left child of node
  def left(self):
    return self.left
  
  # return both children simultaneously
  def children(self):
    return [self.left, self.right]

# balanced binary search tree class
class balancedBinarySearchTree(object):
  # initialize object with a root and size
  # the root is the top element within your binary tree
  def __init__(self, root=None, size =0):
    self.root = root
    self.size =  0
  
  # check if a node is in the tree
  def search(self, n, node = Node(n)):
    nodeLocation = 0
    parent = None
    if self is None
      return False
    elif (node.val == self.val):
      if parent == None:
        print("This number is the root")
        return True
      else:
        print("This number is a child of "+str(parent.root.val))
        return True
    elif (node.val < self.root.val and self.root.left != None):
      parent = self.root
      return self.inTree(self.root.left, node)
    elif (node.val > self.root.val and self.root.right != None):
      parent = self.root
      return self.inTree(self.root.right, node)
    else:
      return False
    
  # insert a node into the tree
  def insert(self, n, node):
    if self.root is None:
        self.root = node
        size += 1
    else:
        if (self.val > node.val):
            if root.left is None:
                root.left = node
            else:
                insert(self.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(self.right, node)

  # delete a value from the tree
  def remove(self, value):
    node = node(value)
    self.remove(self, node)
              
  def remove(self, node):
    if (self.root is None):
       print("The tree is empty.")
    elif (self.root.val == node.val):
       self.root = None
       print(str(node.val)+" was removed.")
    elif (node.val < self.root.val and self.root.left != None):
       remove(self.root.left, node)
    elif (node.val > self.root.val  and self.root.right != None):
       remove(self.root.right, node)
    else:
       print ("This tree doesnt have your value.");
     
