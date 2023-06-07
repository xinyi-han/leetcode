import heapq
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Priority Queue
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = list()
        i = 0
        while head is not None:
            heapq.heappush(nodes, (- head.val, i, head))
            head = head.next
            i += 1
        prev = None
        while len(nodes) > 0:
            _, _, node = heapq.heappop(nodes)
            node.next = prev
            prev = node
        return prev


# Merge Sort
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        r = self.sortList(slow.next)
        slow.next = None
        l = self.sortList(head)
        return self.merge(l, r)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode()
        curr = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1 is not None:
            curr.next = l1
        else:
            curr.next = l2
        return dummy.next
