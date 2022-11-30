from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = list()

        def traverse(node: TreeNode):
            if node is None:
                return
            traverse(node.left)
            nodes.append(node)
            traverse(node.right)

        traverse(root)
        vals = [node.val for node in nodes]
        vals.sort()
        for i, val in enumerate(vals):
            nodes[i].val = val
