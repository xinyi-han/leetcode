from typing import Optional
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = deque()
        while head is not None:
            nodes.append(head)
            head = head.next

        def topDown(flag: int) -> Optional[ListNode]:
            if len(nodes) == 0:
                return None
            if flag == 0:
                node = nodes.popleft()
                flag = 1
            else:
                node = nodes.pop()
                flag = 0
            node.next = topDown(flag)
            return node

        topDown(0)
