from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        curr = head
        while curr is not None:
            if curr.val != val:
                prev.next = curr
                prev = prev.next
            curr = curr.next
        prev.next = None
        return dummy.next
