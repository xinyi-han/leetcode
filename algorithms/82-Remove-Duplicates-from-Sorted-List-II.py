from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashMap = dict()

        def dfs(node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return None
            hashMap[node.val] = hashMap.get(node.val, 0) + 1
            next = dfs(node.next)
            if hashMap[node.val] > 1:
                return next
            node.next = next
            return node

        return dfs(head)
