# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        def dfs(node: TreeNode, x: TreeNode, y: TreeNode):
            if x.val <= node.val <= y.val:
                return node
            if node.val < x.val:
                return dfs(node.right, x, y)
            if node.val > y.val:
                return dfs(node.left, x, y)

        return dfs(root, p, q)
