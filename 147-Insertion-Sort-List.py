from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        while head is not None:
            node = head
            head = head.next
            prev = dummy
            curr = dummy.next
            while curr is not None and curr.val <= node.val:
                prev = curr
                curr = curr.next
            prev.next = node
            node.next = curr
        return dummy.next
