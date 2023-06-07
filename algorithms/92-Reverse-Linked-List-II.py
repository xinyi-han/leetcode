from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        diff = right - left + 1
        slow = dummy
        fast = dummy
        i = 0
        while i < diff:
            fast = fast.next
            i += 1
        j = 1
        while j < left:
            slow = slow.next
            fast = fast.next
            j += 1
        prev = fast.next
        curr = slow.next
        k = 0
        while k < diff:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            k += 1
        slow.next = fast
        return dummy.next
