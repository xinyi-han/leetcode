from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.minD = 9999

        def dfs(node: TreeNode, depth: int):
            if node.left is None and node.right is None:
                self.minD = min(self.minD, depth)
                return
            elif node.left is None:
                dfs(node.right, depth + 1)
            elif node.right is None:
                dfs(node.left, depth + 1)
            else:
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        if root is None:
            return 0
        dfs(root, 1)
        return self.minD
