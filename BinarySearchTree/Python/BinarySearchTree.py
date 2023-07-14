        

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        # If the current node is empty, create a new node with the given key
        if root is None:
            return Node(key)
        
        # If the key is smaller than the current node's key, go to the left subtree
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        # If the key is greater than or equal to the current node's key, go to the right subtree
        else:
            root.right = self._insert_recursive(root.right, key)
        
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        # If the current node is empty or has the desired key, return the node
        if root is None or root.key == key:
            return root
        
        # If the key is smaller than the current node's key, search in the left subtree
        if key < root.key:
            return self._search_recursive(root.left, key)
        
        # If the key is greater than the current node's key, search in the right subtree
        return self._search_recursive(root.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        # If the current node is empty, return it
        if root is None:
            return root
        
        # If the key is smaller than the current node's key, delete in the left subtree
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        # If the key is greater than the current node's key, delete in the right subtree
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # If the current node has no left child, replace it with its right child (or None)
            if root.left is None:
                return root.right
            # If the current node has no right child, replace it with its left child (or None)
            elif root.right is None:
                return root.left
            
            # If the current node has both left and right children, find the minimum node in the right subtree
            min_node = self._find_min_node(root.right)
            # Replace the current node's key with the minimum node's key
            root.key = min_node.key
            # Delete the minimum node from the right subtree
            root.right = self._delete_recursive(root.right, min_node.key)
        
        return root

    def _find_min_node(self, node):
        # Find the leftmost (minimum) node in a subtree
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, root, result):
        # Perform an inorder traversal of the tree (left, root, right)
        if root is not None:
            self._inorder_traversal_recursive(root.left, result)
            result.append(root.key)
            self._inorder_traversal_recursive(root.right, result)
"""
# Test Cases
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:")
print(bst.inorder_traversal())

print("Search for key 40:")
print(bst.search(40))

print("Delete key 40")
bst.delete(40)

print("Inorder traversal after deletion:")
print(bst.inorder_traversal())
        
"""

"""

Binary search trees (BSTs) have a wide range of practical applications. Here are a few common use cases:

Searching and retrieval: BSTs excel at efficient searching and retrieval operations. They allow for fast lookup times, making them suitable for implementing dictionaries, symbol tables, or databases where quick access to data based on a key is required.

Sorting: BSTs can be used to sort data efficiently. By inserting elements into a BST and performing an inorder traversal, the elements can be retrieved in sorted order. This technique is known as the binary tree sort.

Range queries: BSTs support efficient range queries. By performing an inorder traversal between two keys, all elements within a specified range can be retrieved. This property is valuable in scenarios such as database systems where range-based queries are common.

File system organization: BSTs can be used to organize files in a file system. The keys can represent file names or file attributes, and the tree structure can provide efficient searching and ordering capabilities, making it easier to locate and manage files.

Auto-complete and spell checking: BSTs can be employed to implement auto-complete and spell-checking features. By constructing a BST with words or phrases as keys, suggestions can be quickly generated based on partial inputs or misspelled words.

Binary search tree-based algorithms: Various algorithms rely on BSTs as a fundamental data structure. Examples include binary search, balanced binary search trees (such as AVL trees and red-black trees), and self-balancing binary search trees (like B-trees), which are used in database systems to maintain efficient and balanced data storage.

These are just a few examples of practical use cases for binary search trees. The versatility and efficiency of BSTs make them valuable in numerous applications that require fast searching, sorting, and organization of data.
"""