# Balanced Binary Tree Implementation
# Data, Left Child and Right child.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def _create(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
           return self._create(data)
        if data < node.data:
            # smaller ones to the left
            node.left = self.insert(node.left, data)
        else:
            # larger ones to right
            node.right = self.insert(node.right, data)
        return node

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)

    def preOrder(self):
        pass

    def postOrder(self):
        pass