from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True

        def isBalanced_(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l = isBalanced_(node.left)
            r = isBalanced_(node.right)
            if abs(l - r) > 1:
                self.result = False
            return max(l, r) + 1

        isBalanced_(root)
        return self.result
