class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

def printInorder(root): #root in
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def printPreorder(root): #root first
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root): #root last
    if root:
        printPreorder(root.left)
        printPreorder(root.right)
        print(root.val)
'''
    1
   / \
  2   3
 / \
4   5
'''
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Inorder traversal:")
    printInorder(root)
    print("Preorder traversal:")
    printPreorder(root)
    print("Postorder traversal:")
    printPostorder(root)

if __name__ == "__main__":
    main()