class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key


'''
Naive: check if every subtree at every node in tree1 == tree2 -> O(n*m) n = size 1st tree, m = size 2nd tree
Linear time, extra space: 2 traversals to uniquely represent each tree + check if subset  
'''

def preorder(root, l):
    if root:
        l.append(root.val)
        preorder(root.left, l)
        preorder(root.right, l)

def inorder(root, l):
    if root:
        inorder(root.left, l)
        l.append(root.val)
        inorder(root.right, l)


def is_subset(s1, s2):
    if set(s1) & set(s2) == set(s1) or set(s1) & set(s2) == set(s2):
        return True
    return False


def is_subtree(root1, root2):
    l = []
    preorder(root1, l)
    pre_root1 = l

    l = []
    preorder(root2, l)
    pre_root2 = l

    l = []
    inorder(root1, l)
    in_root1 = l

    l = []
    inorder(root2, l)
    in_root2 = l

    if is_subset(pre_root1, pre_root2) and is_subset(in_root1, in_root2):
        return True
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

    root2 = Node(5)
    root2.left = Node(4)
    root2.right = Node(6)

    print(is_subtree(root1, root2))

if __name__ == "__main__":
    main()
