from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancestor = None

        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None or self.ancestor is not None:
                return False
            l = dfs(node.left)
            r = dfs(node.right)
            if ((l and r) or ((l or r) and node in {p, q})):
                self.ancestor = node
                return False
            return l or r or node in {p, q}

        dfs(root)
        return self.ancestor
