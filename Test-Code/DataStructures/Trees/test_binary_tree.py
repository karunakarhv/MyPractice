import unittest
from binarytree import Node, Tree

class BinaryTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        self.rootNode = Node(10)

    def test_insert(self):
        self.tree.insert(self.rootNode, 6)
        self.tree.insert(self.rootNode, 7)
        self.tree.insert(self.rootNode, 8)
        self.tree.insert(self.rootNode, 9)
        self.tree.insert(self.rootNode, 10)
        self.tree.inOrder(self.rootNode)

if __name__ == "":
    unittest.main()