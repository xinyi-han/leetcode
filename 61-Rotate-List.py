from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        node = head
        i = 1
        while node.next is not None:
            i += 1
            node = node.next
        node.next = head
        k %= i
        j = 0
        while j < i - k - 1:
            head = head.next
            j += 1
        node = head.next
        head.next = None
        return node
