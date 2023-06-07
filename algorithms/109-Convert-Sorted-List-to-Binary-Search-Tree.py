from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = list()
        while head is not None:
            vals.append(head.val)
            head = head.next
        return self.buildTree(vals)

    def buildTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        left = self.buildTree(nums[:mid])
        right = self.buildTree(nums[mid+1:])
        return TreeNode(nums[mid], left, right)
