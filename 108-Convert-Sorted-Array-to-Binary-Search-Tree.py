from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = (0 + len(nums) - 1) // 2
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid + 1:])
        node = TreeNode(nums[mid], left, right)
        return node
