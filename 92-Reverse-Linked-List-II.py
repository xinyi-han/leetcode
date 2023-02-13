from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        for i in range(right - left + 1):
            fast = fast.next
        for i in range(left - 1):
            slow = slow.next
            fast = fast.next
        prev = fast.next
        curr = slow.next
        for i in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        slow.next = fast
        return dummy.next
