from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nodes = dict()

        def topDown(node: Node) -> Optional[Node]:
            if node is None:
                return None
            copy = Node(node.val)
            nodes[node] = copy
            copy.next = topDown(node.next)
            if node.random is None:
                copy.random = None
            else:
                copy.random = nodes[node.random]
            return copy

        return topDown(head)
