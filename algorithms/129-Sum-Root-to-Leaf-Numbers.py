from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        output = 0

        def dfs(node: Optional[TreeNode], val: int):
            nonlocal output
            if node.left is None and node.right is None:
                output += val * 10 + node.val
                return
            elif node.left is None:
                dfs(node.right, val * 10 + node.val)
            elif node.right is None:
                dfs(node.left, val * 10 + node.val)
            else:
                dfs(node.left, val * 10 + node.val)
                dfs(node.right, val * 10 + node.val)

        dfs(root, 0)
        return output
