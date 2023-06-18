from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        maxLevel = 0
        level = 1
        nodes = [root]
        while len(nodes) > 0:
            queue = list()
            levelSum = 0
            for node in nodes:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                levelSum += node.val
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level
            nodes = queue
            level += 1
        return maxLevel
