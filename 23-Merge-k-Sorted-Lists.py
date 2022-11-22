from typing import List, Optional
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for node in lists:
            if node is not None:
                heapq.heappush(self.heap, (node.val, self.count, node))
                self.count += 1
        dummy = ListNode()
        head = dummy
        while len(self.heap) > 0:
            val, count, node = heapq.heappop(self.heap)
            head.next = node
            head = head.next
            node = node.next
            if node is not None:
                heapq.heappush(self.heap, (node.val, count, node))
        head.next = None
        return dummy.next
