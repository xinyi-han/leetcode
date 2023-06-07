from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = set()
        while head is not None:
            if head in hashSet:
                return True
            hashSet.add(head)
            head = head.next
        return False
