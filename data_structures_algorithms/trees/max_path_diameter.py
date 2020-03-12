# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 0

    def max_height(self, root: TreeNode) -> int:
        if root is None:
            return 0

        m_left = self.max_height(root.left)
        m_right = self.max_height(root.right)

        max_left_right = max(m_left, m_right) + 1

        #  the path is the depth of the left subtree plus the depth of the right subtree
        self.ans = max(self.ans, m_left + m_right)
        return max_left_right

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_height(root)
        return self.ans

