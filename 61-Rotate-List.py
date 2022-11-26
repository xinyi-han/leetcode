from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        nodes = list()
        while head is not None:
            nodes.append(head)
            head = head.next
        k = k % len(nodes)
        if k == 0:
            return nodes[0]
        nodes[-(k + 1)].next = None
        nodes[-1].next = nodes[0]
        return nodes[-k]
