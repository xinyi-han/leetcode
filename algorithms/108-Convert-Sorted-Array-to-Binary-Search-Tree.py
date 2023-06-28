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
        mid = (len(nums) - 1) // 2
        l = self.sortedArrayToBST(nums[:mid])
        r = self.sortedArrayToBST(nums[mid + 1:])
        root = TreeNode(nums[mid], l, r)
        return root
