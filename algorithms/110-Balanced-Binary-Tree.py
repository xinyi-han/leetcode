from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0, True
            l, lf = dfs(node.left)
            if not lf:
                return 0, False
            r, rf = dfs(node.right)
            if not rf:
                return 0, False
            return max(l, r) + 1, abs(l - r) <= 1

        return dfs(root)[1]
