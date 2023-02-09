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

        def find(node: TreeNode, x: TreeNode, y: TreeNode) -> TreeNode:
            if x.val <= node.val <= y.val:
                return node
            if node.val > y.val:
                return find(node.left, x, y)
            elif node.val < x.val:
                return find(node.right, x, y)

        return find(root, p, q)
