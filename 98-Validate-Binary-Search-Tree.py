from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidBST_(node: Optional[TreeNode], low: float, high: float) -> bool:
            if node is None:
                return True
            if not low < node.val < high:
                return False
            l = isValidBST_(node.left, low, node.val)
            r = isValidBST_(node.right, node.val, high)
            return l and r

        return isValidBST_(root, float('-inf'), float('inf'))
