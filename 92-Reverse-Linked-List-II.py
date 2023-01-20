from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        head = dummy
        for i in range(left - 1):
            head = head.next
            curr = curr.next
        prev = None
        for j in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next.next = curr
        head.next = prev
        return dummy.next
