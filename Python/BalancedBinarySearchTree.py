# python implementation of balanced binary search tree

class node:
    # intialize node class with an intial value, and predefined left child, right child, and parent values
    # the parent is fo rthe sake of the deletion method in the tree class
    def __init__(self, value = None):
    # rather than type out each defined attribute of the class, using a dictionary combined with a magic method
    # accomplishes the same task with only a single line
        # self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
        self._value = value # initialized value of node
        self._left = None # pointer to child with lesser value
        self._right = None # pointer to child node with greater value
        self._parent = None # pointer to parent

    # getters for the node attributes (don't want to make setters because that's what the tree is for)
    # in Python

    @property
    def value(self):
        return self._value
    
    @property
    def left(self):
        return self._left
    
    @property
    def right(self):
        return self._right
    
    @property
    def parent(self):
        return self._parent
    

class binary_search_tree():
    # intialize a tree with a root value and use the dictionary and magic methods approach to store the attribute
    def __init__(self):
        # self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
        self.root = None
    
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

    """
    1. if you need to insert a node past the root, follow this function
    2. if the value of the current node that you're looking at is greater than the value you're attempting to insert
       check the left child, if it is empty, you place the node of the value in as the left child of the current node
    3. else if the value of current node that you're currently looking at is less than the value you're attempting to insert
       check the right child, if it is empty, you place the node of the value in as the right child of the current node
    4. if you've surpassed noth the less than and greater than values, you can assume that you are looking at a node with the same
       value as the one that you're currently looking at, in which case, tell the user that the value is already in the tree
    """
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
    
    """
    return the node object from a tree given a value
    """
    def find(self, value):
        if self.root != None:
            self._find(self, root, cur_node)
        else:
            return False


    def _find(self, cur_node, value):
        if cur_node.value == value:
            return cur_node
        elif cur_node.left != None and cur_node.value > value:
            self._find(self, cur_node.left, value)
        elif cur_node.right != None and cur_node.value < value:
            self._find(self, cur_node.right, value)
        return False

    """
    return boolean of whether a value is in the tree 
    """
    def search(self, value):
        if self.root != None:
            # start by checking if you're looking at nothing, if so, point to the root of your tree
            self._search(self.root, value)
        else:
            return False
    """
    1. call this function in the tree if your root doesn't give you what you need immediately
    2. prioritize successful case first, if the current node has the value that you're looking for, return True
    3. else if the current node that you are looking at is not empty and has a value that is greater than the value you're
    looking at, use the _search function seeting the current node to the left child
    4. else if the current node that you are looking at is not empty and has a value that is less than the value you're
    looking at, use the _search function seeting the current node to the right child
    5. if you've gotten past the conditional statements, you can assume that you're looking at an empty node and therefore can
    return false
    """
    def _search(self, cur_node, value):
        if cur_node.value == value:
            return True
        elif cur_node != None and cur_node.value > value:
            self._search(cur_node.left, value)
        elif cur_node != None and cur_node.value < value:
            self._search(cur_node.right, value)
        return False
      
    """
    refer to https://www.youtube.com/watch?v=Zaf8EOVa72I for help
    1. delete a value from the tree
    """
    """
    def delete(self, value):
        if self.root != None:
            self._delete(self,root,value)
        else:
            return False

    def _delete(self, cur_node, value):
        if cur_node.value == value:
            
        elif cur_node.left != None and cur_node.value > value:
            self._delete(self, cur_node.left, value)
        elif cur_node.right != None and cur_node.value < value:
            self._delete(self, cur_node.right, value)
        return False
    """
        """
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
            if rightHold != None: self.insert(self.root, rightHold)
        # you couldn't find the value in the tree so that means you can't delete it
        # therefore the value isn't in the tree
        else:
            print(str(delVal)+" is not in the tree.")
        """
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


