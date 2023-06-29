from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathSum = float('-inf')

        def dfs(node: Optional[TreeNode]):
            nonlocal pathSum
            if node is None:
                return 0
            l = dfs(node.left)
            l = max(l, 0)
            r = dfs(node.right)
            r = max(r, 0)
            pathSum = max(pathSum, l + r + node.val)
            return max(l, r) + node.val

        dfs(root)
        return pathSum
