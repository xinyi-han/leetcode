from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
        while head is not None and prev is not None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
