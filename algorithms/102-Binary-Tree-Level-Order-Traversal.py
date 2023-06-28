from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = list()
        if root is None:
            return output
        nodes = [root]
        while len(nodes) > 0:
            queue = list()
            vals = list()
            for node in nodes:
                vals.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if len(vals) > 0:
                output.append(vals)
            nodes = queue
        return output
