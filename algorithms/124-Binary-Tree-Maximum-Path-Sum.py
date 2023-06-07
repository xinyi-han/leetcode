from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l = dfs(node.left)
            l = max(l, 0)
            r = dfs(node.right)
            r = max(r, 0)
            self.maxSum = max(self.maxSum, l + r + node.val)
            return max(l, r) + node.val

        dfs(root)
        return self.maxSum
