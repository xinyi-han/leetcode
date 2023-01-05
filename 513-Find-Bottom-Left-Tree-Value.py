from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = list()
        queue.append(root)
        leftMost = None
        while len(queue) > 0:
            level = list()
            leftMost = queue[0].val
            for node in queue:
                if node.left is not None:
                    level.append(node.left)
                if node.right is not None:
                    level.append(node.right)
            queue = level
        return leftMost
