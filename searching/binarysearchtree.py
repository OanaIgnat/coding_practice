"""
binary search property:
the key in each node must be greater than or equal to any key stored in the left sub-tree,
and less than or equal to any key stored in the right sub-tree.

Space complexity:
Avg: O(n)
Worst: O(n)

Search complexity:
Avg: O(log n)
Worst: O(n)

Insert complexity:
Avg: O(log n)
Worst: O(n)

Delete complexity:
Avg: O(log n)
Worst: O(n)
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getChildren(self):
        children = []
        if self.leftChild is not None:
            children.append(self.leftChild)
        if self.rightChild is not None:
            children.append(self.rightChild)
        return children


class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root is None:
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val <= currentNode.val:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif val > currentNode.val:
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if currentNode is None:
            return False
        elif val == currentNode.val:
            return True
        elif val < currentNode.val:
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)
