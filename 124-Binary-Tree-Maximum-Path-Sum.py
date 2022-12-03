from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def postOrder(node: TreeNode) -> int:
            if node is None:
                return 0
            l = postOrder(node.left)
            r = postOrder(node.right)
            # Edge case
            l = max(l, 0)
            r = max(r, 0)
            self.maxSum = max(self.maxSum, l + r + node.val)
            return max(l, r) + node.val

        sum = postOrder(root)
        self.maxSum = max(self.maxSum, sum)
        return int(self.maxSum)
