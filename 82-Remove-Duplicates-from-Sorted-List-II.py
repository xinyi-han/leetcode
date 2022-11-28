from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = list()
        while head is not None:
            if len(nodes) == 0:
                nodes.append(head)
                head = head.next
            else:
                if head.val == nodes[-1].val:
                    while head is not None and head.val == nodes[-1].val:
                        head = head.next
                    nodes.pop()
                else:
                    nodes.append(head)
                    head = head.next
        dummy = ListNode()
        node = dummy
        for n in nodes:
            node.next = n
            node = node.next
        node.next = None
        return dummy.next
