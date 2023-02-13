import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = list()
        for i, node in enumerate(lists):
            if node is None:
                continue
            heapq.heappush(nodes, (node.val, i, node))
        dummy = ListNode()
        curr = dummy
        while len(nodes) > 0:
            val, i, node = heapq.heappop(nodes)
            curr.next = node
            curr = curr.next
            if node.next is not None:
                node = node.next
                heapq.heappush(nodes, (node.val, i, node))
        curr.next = None
        return dummy.next
