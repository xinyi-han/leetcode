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
        queue = [root]
        while len(queue) > 0:
            row = list()
            vals = list()
            for node in queue:
                vals.append(node.val)
                if node.left is not None:
                    row.append(node.left)
                if node.right is not None:
                    row.append(node.right)
            output.append(vals)
            queue = row
        return output
