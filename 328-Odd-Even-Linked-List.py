from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode()
        odd = dummy1
        dummy2 = ListNode()
        even = dummy2
        i = 1
        while head is not None:
            if i % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            i += 1
        even.next = None
        odd.next = dummy2.next
        return dummy1.next
