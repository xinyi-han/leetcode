from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def bfs(l: TreeNode, r: TreeNode) -> bool:
            if l is None and r is None:
                return True
            elif l is None or r is None:
                return False
            elif l.val != r.val:
                return False
            return bfs(l.left, r.right) and bfs(l.right, r.left)

        return bfs(root.left, root.right)
