from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node: Optional[TreeNode], remain: int) -> bool:
            if node is None:
                return False
            if node.left is None and node.right is None:
                if remain == node.val:
                    return True
                return False
            if dfs(node.left, remain - node.val):
                return True
            if dfs(node.right, remain - node.val):
                return True
            return False

        return dfs(root, targetSum)
