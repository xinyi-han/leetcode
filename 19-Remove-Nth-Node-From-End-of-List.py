from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = list()
        while head is not None:
            lst.append(head)
            head = head.next
        if len(lst) == 1:
            return None
        elif n == 1:
            lst[-2].next = None
        elif n == len(lst):
            lst.pop(0)
        else:
            lst[-(n + 1)].next = lst[-n].next
        return lst[0]
