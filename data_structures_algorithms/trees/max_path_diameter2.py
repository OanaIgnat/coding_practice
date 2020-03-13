from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def height_and_diameter(self, root: TreeNode) -> Tuple[int, int]:
        if root is None:
            return 0, 0
        else:
            h_left, d_left = self.height_and_diameter(root.left)
            h_right, d_right = self.height_and_diameter(root.right)

            h = max(h_left, h_right) + 1

            d = max(h_left + h_right, d_left, d_right)

            return h, d

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.height_and_diameter(root)[1]
