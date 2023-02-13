from typing import Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def dfs(node: Optional[ListNode]) -> Tuple[Optional[ListNode], int]:
            if node is None:
                return None, 0
            next, count = dfs(node.next)
            if count + 1 == n:
                return next, count + 1
            else:
                node.next = next
                return node, count + 1

        return dfs(head)[0]
