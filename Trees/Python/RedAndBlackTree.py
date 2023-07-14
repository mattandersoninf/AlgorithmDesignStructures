class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value, "red")  # New nodes are initially red
        if self.root is None:
            self.root = node
        else:
            self._insert_helper(self.root, node)
        self._fix_violations(node)

    def _insert_helper(self, root, node):
        # Helper method to find the appropriate position to insert the new node
        if node.value < root.value:
            if root.left is None:
                root.left = node
                node.parent = root
            else:
                self._insert_helper(root.left, node)
        else:
            if root.right is None:
                root.right = node
                node.parent = root
            else:
                self._insert_helper(root.right, node)

    def _fix_violations(self, node):
        # Fix violations that may have occurred during the insertion process
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                # Case 1: Parent is a left child
                uncle = node.parent.parent.right
                if uncle and uncle.color == "red":
                    # Case 1.1: Uncle is red, recolor nodes
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 1.2: Uncle is black, left rotate
                        node = node.parent
                        self._left_rotate(node)
                    # Case 1.3: Uncle is black, right rotate
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._right_rotate(node.parent.parent)
            else:
                # Case 2: Parent is a right child (symmetric to case 1)
                uncle = node.parent.parent.left
                if uncle and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._left_rotate(node.parent.parent)

        self.root.color = "black"  # Ensure the root is always black

    def _left_rotate(self, node):
        # Perform a left rotation
        new_node = node.right
        node.right = new_node.left
        if new_node.left:
            new_node.left.parent = node
        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        new_node.left = node
        node.parent = new_node

    def _right_rotate(self, node):
        # Perform a right rotation
        new_node = node.left
        node.left = new_node.right
        if new_node.right:
            new_node.right.parent = node
        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.right:
            node.parent.right = new_node
        else:
            node.parent.left = new_node
        new_node.right = node
        node.parent = new_node

    def inorder_traversal(self):
        # Perform an inorder traversal of the red-black tree
        result = []
        self._inorder_traversal_helper(self.root, result)
        return result

    def _inorder_traversal_helper(self, node, result):
        if node:
            self._inorder_traversal_helper(node.left, result)
            result.append(node.value)
            self._inorder_traversal_helper(node.right, result)


# Test cases
tree = RedBlackTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)

# Inorder traversal should return [10, 20, 30, 40, 50]
print(tree.inorder_traversal())