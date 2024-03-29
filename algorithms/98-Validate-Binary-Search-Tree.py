from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode], lb: int, rb: int) -> bool:
            if node is None:
                return True
            if not lb < node.val < rb:
                return False
            return dfs(node.left, lb, node.val) and dfs(node.right, node.val, rb)

        return dfs(root, float('-inf'), float('inf'))
