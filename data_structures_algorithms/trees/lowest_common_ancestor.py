'''
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in T that
has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).

The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest from the root.
Computation of lowest common ancestors may be useful, for instance, as part of a procedure for determining the distance
between pairs of nodes in a tree: the distance from n1 to n2 can be computed as the distance from the root to n1,
plus the distance from the root to n2, minus twice the distance from the root to their lowest common ancestor.

'''

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def findLCA(root, n1, n2):
    # Base Case
    if root is None:
        return None

    # If either n1 or n2 matches with root's key, report the presence by returning root
    if root.key == n1 or root.key == n2:
        return root

    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    if left_lca is not None:
        return left_lca
    else:
        return right_lca

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("LCA(4,5) = ", findLCA(root, 4, 5).val)
    print("LCA(4,6) = ", findLCA(root, 4, 6).val)

if __name__ == "__main__":
    main()