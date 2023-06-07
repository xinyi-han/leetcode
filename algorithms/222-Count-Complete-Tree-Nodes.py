from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        num = 0
        if root is None:
            return num
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                num += 1
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return num
