"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
"""
from coding_practice.data_structures_algorithms.trees.closest_BST_val import TreeNode

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Runtime: 220 ms, faster than 84.31% of Python3 online submissions for Range Sum of BST.
    # Memory Usage: 21 MB, less than 100.00% of Python3 online submissions for Range Sum of BST.
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0

        sum_ = 0
        if root.val >= L and root.val <= R:
            sum_ = root.val

        if root.val >= R or root.val >= L:
            sum_ += self.rangeSumBST(root.left, L, R)
        if root.val <= L or root.val <= R:
            sum_ += self.rangeSumBST(root.right, L, R)

        return sum_

    def rangeSumBST1(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0

        sum_ = 0
        if root.val >= L and root.val <= R:
            sum_ += root.val

        if L < root.val:
            sum_ +=self.rangeSumBST1(root.left, L, R)
        if root.val < R:
            sum_ += self.rangeSumBST1(root.right, L, R)
        return sum_

    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans