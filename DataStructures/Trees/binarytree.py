# Balanced Binary Tree Implementation
# Data, Left Child and Right child.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

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

    def preOrder(self, root):
        if root is not None:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)
    # Given a non-empty binary
    # search tree, return the node
    # with minimum key value
    # found in that tree. Note that the
    # entire tree does not need to be searched


    def minValueNode(self, node):
        current = node
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
        return current

    def deleteNode(self, root, value):
        if root is None:
            return root
        if root.data < value:
            return self.deleteNode(root.right, value)
        if root.data > value:
            return self.deleteNode(root.left, value)
        else:
            # Node has only one child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children
            # Get the inorder successor
            temp = self.minValueNode(root.right)
            # Copy the inorder successor's content to this node
            root.data = temp.data

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.data)

