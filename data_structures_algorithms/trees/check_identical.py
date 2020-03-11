class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def check_identity(root1, root2):
    if root1 is None and root2 is None:
        return True
    if (root1 and root2) and root1.val == root2.val:
        return check_identity(root1.left, root2.left) and check_identity(root1.right, root2.right)
    else:
        return False



'''
    8
   / \
  5   9
 / \
4   6
'''
def main():
    root1 = Node(8)
    root1.left = Node(5)
    root1.right = Node(9)
    root1.left.left = Node(4)
    root1.left.right = Node(6)

    root2 = Node(8)
    root2.left = Node(5)
    root2.right = Node(9)
    root2.left.left = Node(4)
    root2.left.right = Node(6)

    print(check_identity(root1, root2))

if __name__ == "__main__":
    main()