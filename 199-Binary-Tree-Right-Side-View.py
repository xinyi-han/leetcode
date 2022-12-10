from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        output = list()
        while len(queue) > 0:
            num = len(queue)
            val = 0
            for i in range(num):
                node = queue.popleft()
                if node is None:
                    continue
                val = node.val
                queue.append(node.left)
                queue.append(node.right)
            output.append(val)
        return output[:-1]
