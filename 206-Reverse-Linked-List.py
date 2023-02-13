from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


# Recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        def dfs(node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return dummy
            prev = dfs(node.next)
            prev.next = node
            return node

        dfs(head)
        if head is not None:
            head.next = None
        return dummy.next
