from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pair = [0, 0] # [index, value]

        def inOrder(node: Optional[TreeNode]):
            if node is None:
                return
            if pair[0] >= k:
                return
            inOrder(node.left)
            if pair[0] < k:
                pair[0] += 1
                pair[1] = node.val
            inOrder(node.right)

        inOrder(root)
        return pair[-1]
