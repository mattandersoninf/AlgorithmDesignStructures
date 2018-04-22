# python implementation of balanced binary search tree

class node:
    # intialize node class with an intial value, and predefined left child, right child, and parent values
    # the parent is fo rthe sake of the deletion method in the tree class
    def __init__(self, value=None):
    # rather than type out each defined attribute of the class, using a dictionary combined with a magic method
    # accomplishes the same task with only a single line
        # self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
        self.value = value
        self.left = None
        self.right = None

    # getters and setters for the node attributes
    def getValue(self): return self.value
    def getLeftChild(self): return self.left
    def getRightChild(self): return self.right


class binary_search_tree():
    # intialize a tree with a root value and use the dictionary and magic methods approach to store the attribute
    # could expand further if you wish
    # you should intialize the tree with a Node object
    def __init__(self):
        # self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
        self.root = None

    # return the root of the tree
    def getRoot(self):
        return self.root
      
    # set the value of the tre's root
    def setRoot(self, newNode):
        self.root = newNode
    
    def height(self):
        if self.root != None:
            return self._height(self.root,0)

    def _height(self, cur_node, cur_height):
        if cur_node == None : return cur_height
        left_height = self_height(cur_node.left, cur_height+1)
        right_height = self._height(cur_node.right, cur_height+1)
        return max(cur_height, left_height, right_height)


    # insert a new value into the binary search tree
    def insert(self, value):
        if self.root==None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    # if you need to insert a node past the root, follow this function
    def _insert(self, value, cur_node):
        if cur_node.value > value:
            if cur_node.left==None:
                cur_node.left = node(value)
            else:
                self._insert(value, cur_node.left)
        elif cur_node.value < value:
            if cur_node.right==None:
                cur_node.right = node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print "This value is already in the tree!"    
    
       
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
      
    # delete a value from the tree
    def delete(self, root, delVal):
        # initialize holders for the left and right children in case the node your
        # deleting has children
        leftHold = None
        rightHold = None
        # Your search returns something
        if self.search(delVal) != None:
            #  while loop to track down the node
            while root.val != delVal:
                # if the value you want to delete is lower then the value
                # of the node you're currently looking at, look at the left
                # otherwise look at the right
                if delVal < root.val: root = root.left
                else: root = root.right
            # if it has a left or right child, store those nodes with th holders
            if root.left != None: leftHold = root.left
            if root.right != None: rightHold = root.right
            # if the value you're trying to delete is not the root, that parent's pointer
            # to this child is now pointing at nothing which deletes the value from the tree
            if root.parent != None:
                if root.val < root.parent.val: root.parent.left = None
                else: root.parent.right = None
            else:
                self.root = None
            # reinsert the child nodes that were maintained
            if leftHold != None: self.insert(self.root, leftHold)
            if rightHold !=None: self.insert(self.root, rightHold)
        # you couldn't find the value in the tree so that means you can't delete it
        # therefore the value isn't in the tree
        else:
            print(str(delVal)+" is not in the tree.")
    #------------------------------------------------------------------------------
    # Traversals
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


