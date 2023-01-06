from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node: TreeNode) -> str:
            if node is None:
                return ""
            left = dfs(node.left)
            right = dfs(node.right)
            if left == "" and len(right) > 0:
                left = "()"
            return "(" + str(node.val) + left + right + ")"

        s = dfs(root)
        return s[1:-1]
