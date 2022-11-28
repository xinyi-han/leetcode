from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        newHead = head
        node = newHead
        while head is not None:
            if head.val != node.val:
                node.next = head
                node = node.next
            head = head.next
        node.next = None
        return newHead
