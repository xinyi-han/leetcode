from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + carry
            carry = val // 10
            val %= 10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        if l1 is not None:
            l = l1
        else:
            l = l2
        while l is not None:
            val = l.val + carry
            carry = val // 10
            val %= 10
            curr.next = ListNode(val)
            curr = curr.next
            l = l.next
        if carry != 0:
            curr.next = ListNode(carry)
        return dummy.next
