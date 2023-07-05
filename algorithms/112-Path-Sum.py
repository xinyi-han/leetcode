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
            sum += node.val
            if node.left is None and node.right is None:
                return True if sum == targetSum else False
            elif node.left is None:
                return dfs(node.right, sum)
            elif node.right is None:
                return dfs(node.left, sum)
            else:
                return dfs(node.left, sum) or dfs(node.right, sum)

        if root is None:
            return False
        return dfs(root, 0)
