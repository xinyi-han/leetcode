from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = list()
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            level = list()
            for i in range(len(queue)):
                node = queue.popleft()
                if node is not None:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(level) > 0:
                output.append(level)
        return output
