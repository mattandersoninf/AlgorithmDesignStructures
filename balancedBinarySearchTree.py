# insert, delete, search methods for tree node
#

class Node:
    def __init__(self, val = None, r = None, l = None, p = None, red = None):
        self.v = val                # value in node
        self.r = r                  # right child
        self.l = l                  # left child
        self.p = p                  # parent node
        self.red = red              # red boolean to keep track of balance

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, val):
        insertNode = Node(val)
        if(self.root == None):
            self.root = insertNode
        else:
            self._insert(insertNode, self.root)

    def _insert(self, insertNode, parentNode):
        if parentNode.val > insertNode.val:
            if parentNode.l != None:
                insertNode.p = parentNode
                parentNode.l = insertNode
            else:
                
        elif parentNode.val < insertNode.val and parentNode.r != None:
            insertNode.p = parentNode
            parentNode.r = insertNode
        else:
            return
            
            

    def search(self, val):
        if(self.root != None):
            return self._search(val, self.root)
        else:
            return None

    def _search(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._search(val, node.l)
        elif(val > node.v and node.r != None):
            self._search(val, node.r)

    # return minimum value in tree
    def min(self):
        if self.root == None:
            return None
        else:
           return self._min(self.root)
    
    def _min(self, node):
        while node.l != None:
            self._min(node.l)
        return node

    # return maximum value in tree
    def max(self):
        if self.root == None:
            return None
        else:
           return _max(self.root)
    
    def _max(self, node):
        while node.r != None:
            _max(node.r)
        return node
        
    # delete node from tree
    def delete(self, val):
        if self == None:
            return None
        else:
            return self._delete(self.root, val)
    
   #adjust so that the node class does the heavy liftiing 
    def _delete(self, node, val):
        if node == None:
            return
        elif node.val != val:
            if node.val < val:
                self._delete(node.l,val)
            else:
                self._delete(node.r,val)
        else:
            if node.l != None:
                temp = node
                node.l = node
                node.p = temp
            
            

    def transplant(self, node, newnode):
        if node.p == None:
            self.root = newnode
        elif node == node.p.l:
            node.p.l = newnode
        else:
            node.p.r = newnode
        if newnode != None:
            newnode.p = node.p
            
            
            
            
            
            
    # rotate values left within a subtree about node x
    def _left_rotate(self, x):
        "Left rotate x."
        y = x.right
        x._right = y.left
        if y.left != self.nil:
            y.left._p = x
        y._p = x.p
        if x.p == self.nil:
            self._root = y
        elif x == x.p.left:
            x.p._left = y
        else:
            x.p._right = y
        y._left = x
        x._p = y

    # rotate values right within a subtree about node x
    def _right_rotate(self, y):
        "Left rotate y."
        x = y.left
        y._left = x.right
        if x.right != self.nil:
            x.right._p = y
        x._p = y.p
        if y.p == self.nil:
            self._root = x
        elif y == y.p.right:
            y.p._right = x
        else:
            y.p._left = x
        x._right = y
        y._p = x

    # make sure the tree is balanced
    def check_invariants(self):
        "@return: True iff satisfies all criteria to be red-black tree."
        
        def is_red_black_node(node):
            "@return: num_black"
            # check has _left and _right or neither
            if (node.left and not node.right) or (node.right and not node.left):
                return 0, False

            # check leaves are black
            if not node.left and not node.right and node.red:
                return 0, False

            # if node is red, check children are black
            if node.red and node.left and node.right:
                if node.left.red or node.right.red:
                    return 0, False
                    
            # descend tree and check black counts are balanced
            if node.left and node.right:
                
                # check children's parents are correct
                if self.nil != node.left and node != node.left.p:
                    return 0, False
                if self.nil != node.right and node != node.right.p:
                    return 0, False

                # check children are ok
                left_counts, left_ok = is_red_black_node(node.left)
                if not left_ok:
                    return 0, False
                right_counts, right_ok = is_red_black_node(node.right)
                if not right_ok:
                    return 0, False

                # check children's counts are ok
                if left_counts != right_counts:
                    return 0, False
                return left_counts, True
            else:
                return 0, True
                
        num_black, is_ok = is_red_black_node(self.root)
        return is_ok and not self.root._red

def test_tree(t, keys):
    "Insert keys one by one checking invariants and membership as we go."
    assert t.check_invariants()
    for i, key in enumerate(keys):
        for key2 in keys[:i]:
            assert t.nil != t.search(key2)
        for key2 in keys[i:]:
            assert (t.nil == t.search(key2)) ^ (key2 in keys[:i])
        t.insert_key(key)
        assert t.check_invariants()
    

if '__main__' == __name__:
    import os, sys, numpy.random as R
    def write_tree(t, filename):
        "Write the tree as an SVG file."
        f = open('%s.dot' % filename, 'w')
        write_tree_as_dot(t, f)
        f.close()
        os.system('dot %s.dot -Tsvg -o %s.svg' % (filename, filename))
        
    # test the rbtree
    R.seed(2)
    size=50
    keys = R.randint(-50, 50, size=size)
    t = rbtree()
    test_tree(t, keys)
    write_tree(t, 'tree')

 
