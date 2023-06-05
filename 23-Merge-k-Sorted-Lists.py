import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = list()
        heapq.heapify(heap)
        for i, l in enumerate(lists):
            if l is None:
                continue
            heapq.heappush(heap, (l.val, i, l))
        dummy = ListNode()
        node = dummy
        while len(heap) > 0:
            val, i, l = heapq.heappop(heap)
            node.next = l
            node = node.next
            l = l.next
            if l is not None:
                heapq.heappush(heap, (l.val, i, l))
        return dummy.next
