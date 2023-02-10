from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node: Optional[TreeNode], sum: int) -> bool:
            if node.left is None and node.right is None:
                if sum + node.val == targetSum:
                    return True
                return False
            sum += node.val
            if node.left is None:
                if dfs(node.right, sum):
                    return True
            elif node.right is None:
                if dfs(node.left, sum):
                    return True
            else:
                if dfs(node.left, sum):
                    return True
                if dfs(node.right, sum):
                    return True
            return False

        if root is None:
            return False
        return dfs(root, 0)
