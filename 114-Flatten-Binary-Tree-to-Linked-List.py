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
        if root is None:
            return None
        stack = list()
        node = root
        while node is not None:
            if node.left is None and node.right is None:
                if len(stack) == 0:
                    break
                node.right = stack.pop()
                node = node.right
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node.right = node.left
                node.left = None
                node = node.right
            else:
                stack.append(node.right)
                node.right = node.left
                node.left = None
                node = node.right
