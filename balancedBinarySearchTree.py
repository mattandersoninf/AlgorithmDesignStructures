import random
import subprocess

class node(object):
  # initialize a node with key and a a set velue
  def init(self, key, value):
      self.key = key
      self.value = value
      self._left = None
      self._right = None
  
  # generate right side of node
  def right(self):
      return self._right
  # set value of right side of node
  @right.setter
  def right(self, value):
      self._right = value

  # generate left side of node
  @property
  def left(self):
      return self._left

  #set value of left side of node
  @left.setter
  def left(self, value):
      self._left = value

# balanced binary search tree class
class balancedBinarySearchTree(object):
  def __init__(self, key_func=lambda x: id(x)):
        self._root = None
        self._key_func = key_func

    def _insert(self, node, subtree):
        if node.key <= subtree.key:
            if subtree.left is None:
                subtree.left = node
            else:
                self._insert(node, subtree.left)
        else:
            if subtree.right is None:
                subtree.right = node
            else:
                self._insert(node, subtree.right)

    def insert(self, value):
        node = Node(self._key_func(value), value)
        if self._root is None:
            self._root = node
        else:
            self._insert(node, self._root)

    def _left_to_right(self, subtree):
        if subtree is None:
            return

        for i in self._left_to_right(subtree.left):
            yield i

        yield subtree.value

        for i in self._left_to_right(subtree.right):
            yield i

    def _balance(self, subtree, element_list):
        if not element_list:
            return
        right_list_length = len(element_list)/2
        value = element_list[right_list_length]
        node = Node(self._key_func(value), value)
        self._insert(node, subtree)
        self._balance(node, element_list[:right_list_length])
        self._balance(node, element_list[right_list_length+1:])

    def balance(self):
        sorted_elements = list(self._left_to_right(self._root))

        if not sorted_elements:
            self._root = None
            return

        right_list_length = len(sorted_elements)/2
        value = sorted_elements[right_list_length]
        node = Node(self._key_func(value), value)
        self._root = node
        self._balance(node, sorted_elements[:right_list_length])
        self._balance(node, sorted_elements[right_list_length+1:])s
