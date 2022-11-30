from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = list()

        def dfs(node: TreeNode):
            if node is None:
                return
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                node.right = node.left
                node.left = None
            else:
                if len(stack) > 0:
                    node.right = stack.pop()
                else:
                    node.right = None
            dfs(node.right)

        if root is None:
            return None
        dfs(root)
