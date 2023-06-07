from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = dict()

        def dfs(node: Optional[Node]) -> Optional[Node]:
            if node is None:
                return None
            copy = Node(node.val)
            nodes[node] = copy
            copy.next = dfs(node.next)
            if node.random is not None:
                copy.random = nodes[node.random]
            return copy

        return dfs(head)
