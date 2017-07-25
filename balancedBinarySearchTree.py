
# refernece for dict structure
# self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
class Node(object):
  # initialize a node with key and a a set velue
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.right = right
    self.left =  left
  # return both children simultaneously
  def children(self):
    return [self.left, self.right]

# balanced binary search tree class
class balancedBinarySearchTree(object):
  # initialize object with a root and size
  # the root is the top element within your binary tree
  def __init__(self, root=None, size =0):
    self.root = root
    self.size = size
  
  # check if a node is in the tree
  def search(self, node):
    nodeLocation = 0
    parent = None
    if self is None:
      return False
    elif (node.val == self.root.val):
      if parent == None:
        print("This number is the root")
        return True
      else:
        print("This number is in node: "+str(nodeLocation))
        print("This number is a child of: "+str(parent.root.val))
        return True
    elif (node.val < self.root.val and self.root.left != None):
      parent = self.root
      return self.search(node)
    elif (node.val > self.root.val and self.root.right != None):
      parent = self.root
      return self.search(node)
    else:
      return False
    
  # insert a node into the tree
  def insert(self, node):
    if self.root is None:
        self.root = node
        self.size += 1
    else:
        if (self.root.val > node.val):
            if self.root.left is None:
                self.root.left = node
            else:
                self.root.left.insert(node)
        else:
            if self.root.right is None:
                self.root.right = node
            else:
                self.root.right.insert(node)

  # delete a value from the tree
  def remove(self, node):
    if (self.root is None):
       print("The tree is empty.")
    elif (self.root.val == node.val):
       self.root = None
       print(str(node.val)+" was removed.")
    elif (node.val < self.root.val and self.root.left != None):
       self.root.left.remove(node)
    elif (node.val > self.root.val  and self.root.right != None):
       self.root.right.remove(node)
    else:
       print ("This tree doesnt have your value.");


def main():
  a = Node(3)
  b = Node(6)
  c = Node(1)
  d = Node(4)
  e = Node(8)
  f = Node(2)
  
  balancedBinarySearchTree.__init__(a)
  balancedBinarySearchTree.insert(b)  
  balancedBinarySearchTree.insert(c)
  balancedBinarySearchTree.insert(d)  
  balancedBinarySearchTree.insert(e)
  balancedBinarySearchTree.insert(f)
  
