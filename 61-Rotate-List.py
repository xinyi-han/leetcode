from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        i = 0
        while curr is not None:
            i += 1
            curr = curr.next
        k %= i
        if k == 0:
            return head
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        for j in range(k - 1):
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        head = slow.next
        slow.next = None
        fast.next = dummy.next
        return head
