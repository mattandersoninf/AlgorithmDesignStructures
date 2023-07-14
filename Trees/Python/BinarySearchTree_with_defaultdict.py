from collections import defaultdict

class BST:
    def __init__(self):
        # Use a defaultdict with default value [None, None] to store the BST nodes
        self.tree = defaultdict(lambda: [None, None])

    def insert(self, key):
        if self.tree[key][0] is None:
            # If the current node is empty, set it as the new key
            self.tree[key][0] = key
        else:
            # Otherwise, recursively find the appropriate position to insert the key
            self.insert_recursive(key, self.tree[key][0])

    def insert_recursive(self, key, current):
        if key < current:
            if self.tree[current][0] is None:
                # If the left child of the current node is empty, insert the key as the left child
                self.tree[current][0] = key
            else:
                # Otherwise, continue searching for the appropriate position in the left subtree
                self.insert_recursive(key, self.tree[current][0])
        else:
            if self.tree[current][1] is None:
                # If the right child of the current node is empty, insert the key as the right child
                self.tree[current][1] = key
            else:
                # Otherwise, continue searching for the appropriate position in the right subtree
                self.insert_recursive(key, self.tree[current][1])

    def search(self, key):
        # Start the recursive search from the root of the tree
        return self.search_recursive(key, next(iter(self.tree)))

    def search_recursive(self, key, current):
        if current is None or key == current:
            # If the current node is empty or has the desired key, return the current node
            return current
        if key < current:
            # If the key is smaller than the current node's key, search in the left subtree
            return self.search_recursive(key, self.tree[current][0])
        # If the key is greater than the current node's key, search in the right subtree
        return self.search_recursive(key, self.tree[current][1])

    def delete(self, key):
        if key not in self.tree:
            # If the key is not found in the tree, return
            return
        # Start the recursive deletion from the root of the tree
        self.delete_recursive(key, next(iter(self.tree)))

    def delete_recursive(self, key, current):
        if current is None:
            # If the current node is empty, return
            return
        if key < current:
            # If the key is smaller than the current node's key, delete in the left subtree
            self.delete_recursive(key, self.tree[current][0])
        elif key > current:
            # If the key is greater than the current node's key, delete in the right subtree
            self.delete_recursive(key, self.tree[current][1])
        else:
            # If the current node matches the key to be deleted
            left, right = self.tree[current]
            if left is None and right is None:
                # If the current node has no children, set it as empty
                self.tree[current] = [None, None]
            elif left is None:
                # If the current node has no left child, replace it with the right child
                self.tree[current] = self.tree[right]
            elif right is None:
                # If the current node has no right child, replace it with the left child
                self.tree[current] = self.tree[left]
            else:
                # If the current node has both left and right children
                replacement = self.find_minimum(right)
                # Find the minimum node in the right subtree
                self.tree[current] = [replacement, self.tree[right]]
                # Replace the current node's key with the minimum node's key
                self.delete_recursive(replacement, right)
                # Delete the minimum node from the right subtree

    def find_minimum(self, current):
        # Find the minimum node in a subtree (leftmost node)
        while self.tree[current][0] is not None:
            current = self.tree[current][0]
        return current