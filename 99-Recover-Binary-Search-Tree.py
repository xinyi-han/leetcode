from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        vals = list()

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)
        vals.sort()
        stack = list()
        node = root
        i = 0
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.val = vals[i]
            node = node.right
            i += 1
