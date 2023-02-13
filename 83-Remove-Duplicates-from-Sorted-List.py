from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0, head)
        prev = head
        curr = head
        while curr is not None:
            if prev.val != curr.val:
                prev.next = curr
                prev = prev.next
            curr = curr.next
        prev.next = None
        return dummy.next
