import BalancedBinarySearchTree
# you only need one of these test libraries but try both and see which you prefers
import unittest
import pytest


"""
use this section for utilizing pytest
"""
# intial testing to prove insert, search, and delete functions work
mainTree = Tree(Node(5))
print(mainTree.root)
print(mainTree.search(5))
mainTree.insert(mainTree.root, Node(3))
print(mainTree.search(3))
mainTree.insert(mainTree.root, Node(4))
print(str(mainTree.search(4))+": node for 4")
mainTree.insert(mainTree.root, Node(1))
print(str(mainTree.search(1))+": node for 1")
mainTree.deleteVal(mainTree.root, 3)
print(mainTree.search(3))
print(mainTree.search(4))
print(mainTree.search(1))
mainTree.insert(mainTree.root, Node(7))
print(str(mainTree.root.left.val)+": if done properly, this should be 1.")
print(str(mainTree.root.left.right.val)+": if done properly, this should be 4.")
#mainTree.preorder(mainTree.root)
#mainTree.inorder(mainTree.root)
#mainTree.postorder(mainTree.root)


"""
mainTree.insert(2)
mainTree.insert(4)
mainTree.insert(1)
print("search 1's value is "+str(mainTree.search(1)))
print("search 2's value is "+str(mainTree.search(2)))
mainTree.insert(5)
mainTree.delete(2)
print("search 2's value is "+str(mainTree.search(2)))
mainTree.insert(1)
mainTree.search(1)
"""



"""
use this section for testing with unittest
"""