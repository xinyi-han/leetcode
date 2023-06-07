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

        def dfs(node: ListNode) -> Optional[ListNode]:
            if node.next is None:
                dummy.next = node
                return node
            prev = dfs(node.next)
            prev.next = node
            return node

        if head is None:
            return head
        tail = dfs(head)
        tail.next = None
        return dummy.next
