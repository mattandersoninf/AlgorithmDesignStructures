# Node class represents each node in the binary tree
class Node:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.left = None  # Reference to the left child node
        self.right = None  # Reference to the right child node

# Binary tree class represents the binary tree as a whole
class BinaryTree:
    def __init__(self):
        self.root = None  # Reference to the root node of the tree

    def insert(self, data):
        # If the tree is empty, create a new node as the root
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        # Recursively find the appropriate position to insert the new node
        if data < node.data:
            if node.left is None:
                node.left = Node(data)  # Create a new node as the left child
            else:
                self._insert_recursive(data, node.left)  # Recurse on the left subtree
        else:
            if node.right is None:
                node.right = Node(data)  # Create a new node as the right child
            else:
                self._insert_recursive(data, node.right)  # Recurse on the right subtree

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        # Recursively search for a node with the given value
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(data, node.left)  # Recurse on the left subtree
        return self._search_recursive(data, node.right)  # Recurse on the right subtree

# Create a binary tree instance
tree = BinaryTree()

# Insert nodes into the binary tree
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Search for a node with a specific value
result = tree.search(6)
if result is not None:
    print("Node found with value:", result.data)
else:
    print("Node not found")