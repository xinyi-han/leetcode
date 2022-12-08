from typing import Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.heap = list()
        self.count = 0

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head is not None:
            heapq.heappush(self.heap, (head.val, self.count, head))
            self.count += 1
            head = head.next
        dummy = ListNode()
        curr = dummy
        while len(self.heap) > 0:
            _, _, node = heapq.heappop(self.heap)
            curr.next = node
            curr = curr.next
        curr.next = None
        return dummy.next
