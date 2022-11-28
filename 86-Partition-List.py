from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        left = ListNode()
        node1 = left
        right = ListNode()
        node2 = right
        while head is not None:
            if head.val < x:
                node1.next = head
                node1 = node1.next
            else:
                node2.next = head
                node2 = node2.next
            head = head.next
        node2.next = None
        node1.next = right.next
        return left.next
