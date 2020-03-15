# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: abs(target - x))
            if target < root.val:
                root = root.left
            else:
                root = root.right
            # root = root.left if target < root.val else root.right

        return closest

