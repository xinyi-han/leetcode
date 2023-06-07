from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = list()
        if root is None:
            return output
        queue = [root]
        i = 0
        while len(queue) > 0:
            level = list()
            vals = list()
            for node in queue:
                vals.append(node.val)
                if node.left is not None:
                    level.append(node.left)
                if node.right is not None:
                    level.append(node.right)
            queue = level
            if len(vals) > 0:
                if i % 2 == 1:
                    output.append(vals[::-1])
                else:
                    output.append(vals)
            i += 1
        return output
