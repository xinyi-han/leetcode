# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancestor = None

        def traverse(node: 'TreeNode', i: 'TreeNode', j: 'TreeNode') -> bool:
            if node is None or self.ancestor is not None:
                return False
            left = traverse(node.left, i, j)
            right = traverse(node.right, i, j)
            if node == i or node == j:
                if not left and not right:
                    return True
                elif left or right:
                    self.ancestor = node
                    return False
            elif left and right:
                self.ancestor = node
                return False
            elif left or right:
                return True

        traverse(root, p, q)
        return self.ancestor
