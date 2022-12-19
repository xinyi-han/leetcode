from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cache = [0, -1] # [index, val]

        def traverse(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            if traverse(node.left):
                return True
            cache[0] += 1
            cache[1] = node.val
            if cache[0] == k:
                return True
            if traverse(node.right):
                return True
            return False

        traverse(root)
        return cache[-1]
