from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetric_(root.left, root.right)

    def isSymmetric_(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.isSymmetric_(p.left, q.right) and self.isSymmetric_(p.right, q.left)
