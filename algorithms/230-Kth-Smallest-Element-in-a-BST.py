from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = list()

        def inorder(node: Optional[TreeNode]) -> bool:
            if len(vals) == k:
                return True
            if node is None:
                return False
            if inorder(node.left):
                return True
            vals.append(node.val)
            if inorder(node.right):
                return True
            return False

        inorder(root)
        return vals[-1]
