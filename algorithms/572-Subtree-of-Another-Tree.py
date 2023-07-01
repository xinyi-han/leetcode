from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if r1 is None and r2 is None:
            return True
        elif r1 is None or r2 is None or r1.val != r2.val:
            return False
        else:
            return self.isSameTree(r1.left, r2.left) and self.isSameTree(r1.right, r2.right)
