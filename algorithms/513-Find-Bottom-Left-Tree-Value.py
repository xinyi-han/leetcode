from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        nodes = [root]
        val = root.val
        while len(nodes) > 0:
            queue = list()
            for node in nodes:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            val = nodes[0].val
            nodes = queue
        return val
