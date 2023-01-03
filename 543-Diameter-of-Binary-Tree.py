from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def bottomUp(node: TreeNode) -> int:
            if node is None:
                return 0
            left = bottomUp(node.left)
            right = bottomUp(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        bottomUp(root)
        return self.diameter
