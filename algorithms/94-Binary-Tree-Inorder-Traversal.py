from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = list()

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)
        return vals


# Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = list()
        stack = list()
        node = root
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            output.append(node.val)
            node = node.right
        return output
