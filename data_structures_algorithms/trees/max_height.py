
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


'''
Recursively compute max height of left & right subtrees
Get the maximum between them
Add 1 for the current node
'''
def height(root):
    if root is None:
        return 0
    else:
        h_left = height(root.left)
        h_right = height(root.right)
        return max(h_left, h_right) + 1  # +1 for current node


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

    print(height(root))

if __name__ == "__main__":
    main()