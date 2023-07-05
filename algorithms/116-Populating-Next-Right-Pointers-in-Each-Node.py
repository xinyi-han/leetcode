from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        node = root
        while node.left is not None:
            parent = node
            while parent.next is not None:
                parent.left.next = parent.right
                parent.right.next = parent.next.left
                parent = parent.next
            parent.left.next = parent.right
            node = node.left
        return root
