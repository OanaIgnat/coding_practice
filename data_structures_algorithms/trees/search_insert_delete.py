'''
- always check tree exists: root is not None
- value != node: search for a value, insert a node
- initialize class Node with left, right, val
- start with root Node, add root.left and root.right

'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# search for a value
def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val > key:
        search(root.left, key)
    else:
        search(root.right, key)

# insert a node
# A new node is always inserted at the leaf
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)


def delete(root, node):
    if root is None:
        return
    if root == node:
        del root
    if root.val < node.val:
        delete(root.right, node)
    else:
        delete(root.left, node)



def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)



'''
    8
   / \
  5   9
 / \
4   6
'''
def main():
    root = Node(8)
    root.left = Node(5)
    root.right = Node(9)
    root.left.left = Node(4)
    root.left.right = Node(6)

    print(search(root, 2))
    insert(root, Node(2))
    inorder_traversal(root)
    delete(root, Node(2))
    print("After delete node 2:")
    inorder_traversal(root)

if __name__ == "__main__":
    main()


