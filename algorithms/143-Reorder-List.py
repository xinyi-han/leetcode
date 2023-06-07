from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        while fast is not None and fast.next is not None:
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
        curr = dummy
        while head is not None and prev is not None:
            curr.next = head
            curr = curr.next
            head = head.next
            curr.next = prev
            curr = curr.next
            prev = prev.next
        if head is not None:
            curr.next = head
        elif prev is not None:
            curr.next = prev
