from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        output = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal output
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            output = max(output, l + r)
            return max(l, r) + 1

        dfs(root)
        return output
