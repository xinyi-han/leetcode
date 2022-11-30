from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node: TreeNode, sum: int) -> bool:
            val = node.val
            l = False
            r = False
            if node.left is None and node.right is None:
                if sum + val == targetSum:
                    return True
                return False
            elif node.left is None:
                r = dfs(node.right, sum + val)
            elif node.right is None:
                l = dfs(node.left, sum + val)
            else:
                l = dfs(node.left, sum + val)
                r = dfs(node.right, sum + val)
            if l or r:
                return True
            return False

        if root is None:
            return False
        return dfs(root, 0)
