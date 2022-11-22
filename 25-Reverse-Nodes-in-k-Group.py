from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        nodes = list()
        for i in range(k):
            if node is None:
                return head
            nodes.append(node)
            node = node.next
        dummy = ListNode()
        head = dummy
        while len(nodes) > 0:
            head.next = nodes.pop()
            head = head.next
        head.next = self.reverseKGroup(node, k)
        return dummy.next
