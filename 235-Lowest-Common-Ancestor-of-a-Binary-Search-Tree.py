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

        def traverse(node: 'TreeNode', i: 'TreeNode', j: 'TreeNode') -> 'TreeNode':
            if i.val <= node.val <= j.val:
                return node
            elif node.val > j.val:
                return traverse(node.left, i, j)
            elif node.val < i.val:
                return traverse(node.right, i, j)

        return traverse(root, p, q)
