class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        # Perform the standard BST insertion
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        # Update the height of the current node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Check the balance factor and perform necessary rotations if the tree becomes unbalanced
        balance = self._get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        # Perform standard BST deletion
        if not root:
            return root
        elif key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node to be deleted found
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = self._get_min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        # Update the height of the current node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Check the balance factor and perform necessary rotations if the tree becomes unbalanced
        balance = self._get_balance(root)

        if balance > 1:
            if self._get_balance(root.left) >= 0:
                return self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)

        if balance < -1:
            if self._get_balance(root.right) <= 0:
                return self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)

        return root

    def _left_rotate(self, z):
        # Perform a left rotation
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Update the heights of the rotated nodes
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        # Perform a right rotation
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Update the heights of the rotated nodes
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        # Get the height of a node
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        # Get the balance factor of a node
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_min_value_node(self, node):
        # Get the node with the minimum key value in the given subtree
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)

    def pre_order(self):
        # Preorder traversal of the tree
        self._pre_order(self.root)

    def _pre_order(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self._pre_order(root.left)
        self._pre_order(root.right)
        
"""
tree = AVLTree()

tree.insert(9)
tree.insert(5)
tree.insert(10)
tree.insert(0)
tree.insert(6)
tree.insert(11)
tree.insert(-1)
tree.insert(1)
tree.insert(2)

print("Preorder Traversal:")
tree.pre_order()
print()

tree.delete(10)

print("Preorder Traversal after deleting 10:")
tree.pre_order()
print()
"""