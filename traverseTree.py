    
# tree traversals
class traverseTree:
  def preorder(self,tree):
      if tree:
          print(tree._p)
          preorder(tree._left)
          preorder(tree._right)


  def postorder(self,tree):
      if tree != None:
          postorder(tree._left)
          postorder(tree._right)
          print(tree._p)


  def inorder(self,tree):
    if tree != None:
        inorder(tree._left)
        print(tree._p)
        inorder(tree._right)
