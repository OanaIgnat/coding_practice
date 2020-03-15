"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.
Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
"""
from coding_practice.data_structures_algorithms.trees.closest_BST_val import TreeNode


class Solution:
    # Runtime: 32 ms, faster than 44.33% of Python3 online submissions for Minimum Distance Between BST Nodes.
    # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Minimum Distance Between BST Nodes.
    def minDiffInBST1(self, root: TreeNode) -> int:
        v = []  # O(n) space complexity

        def dfs(node):
            if node:
                v.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        v.sort()  # O(nlog n) time complexity

        min_v = float("inf")
        for i in range(len(v) - 1):
            min_v = min(min_v, v[i + 1] - v[i])

        return min_v

    # instead of DFS, do inorder traversal -> already ordered
    # Runtime: 28 ms, faster than 76.92% of Python3 online submissions for Minimum Distance Between BST Nodes.
    # Memory Usage: 13.1 MB, less than 92.31% of Python3 online submissions for Minimum Distance Between BST Nodes.
    def minDiffInBST2(self, root: TreeNode) -> int:
        v = []  # O(n) space complexity

        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                v.append(node.val)
                inorder_traversal(node.right)

        inorder_traversal(root)

        min_v = float("inf")
        for i in range(len(v) - 1):
            min_v = min(min_v, v[i + 1] - v[i])

        return min_v
