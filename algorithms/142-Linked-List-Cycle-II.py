from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashSet = set()
        while head is not None:
            if head in hashSet:
                return head
            hashSet.add(head)
            head = head.next
        return None
