from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        vals = list()
        while node is not None:
            vals.append(node.val)
            node = node.next
        vals.sort()
        node = head
        i = 0
        while i < len(vals):
            node.val = vals[i]
            node = node.next
            i += 1
        return head
