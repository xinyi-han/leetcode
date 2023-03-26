from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        heights = set()

        def dfs(node: Optional[TreeNode], h: int):
            if node is None:
                return
            if node.left is None and node.right is None:
                heights.add(h)
                return
            dfs(node.left, h + 1)
            dfs(node.right, h + 1)

        dfs(root, 1)
        return min(heights)
