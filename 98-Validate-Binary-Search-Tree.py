# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def bfs(node: TreeNode, lower: float, upper: float) -> bool:
            if node is None:
                return True
            if not lower < node.val < upper:
                return False
            return bfs(node.left, lower, node.val) and bfs(node.right, node.val, upper)

        return bfs(root, float('-inf'), float('inf'))
