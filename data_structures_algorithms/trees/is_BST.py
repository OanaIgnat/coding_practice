# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def check(node, lower = float('-inf'), upper = float('inf')):
            
            if not node:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            if not check(node.right, val, upper):
                return False
            if not check(node.left, lower, val):
                return False
            return True
        
        return check(root)
