from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode()
        prev, curr = dummy, head
        while curr is not None and curr.next is not None:
            prev.next = curr.next
            prev = prev.next
            next = prev.next
            prev.next = curr
            prev = curr
            curr = next
        prev.next = curr
        return dummy.next
