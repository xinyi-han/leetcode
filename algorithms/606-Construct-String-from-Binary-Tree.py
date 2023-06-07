from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node: Optional[TreeNode]) -> str:
            if node.left is None and node.right is None:
                return "(" + str(node.val) + ")"
            elif node.left is None:
                r = dfs(node.right)
                return "(" + str(node.val) + "()" + r + ")"
            elif node.right is None:
                l = dfs(node.left)
                return "(" + str(node.val) + l + ")"
            else:
                l = dfs(node.left)
                r = dfs(node.right)
                return "(" + str(node.val) + l + r + ")"

        s = dfs(root)
        return s[1:-1]
