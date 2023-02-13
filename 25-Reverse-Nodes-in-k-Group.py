from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for i in range(k):
            if curr is None:
                return head
            curr = curr.next
        prev = self.reverseKGroup(curr, k)
        curr = head
        for i in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
