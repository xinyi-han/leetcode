from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        slow.next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        output = 0
        while head is not None:
            output = max(output, head.val + prev.val)
            head = head.next
            prev = prev.next
        return output
