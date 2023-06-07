# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        stack = list()
        stack.append(root)
        while len(stack) > 0:
            level = list()
            prev = None
            for i in range(len(stack)):
                node = stack.pop()
                if node is None:
                    continue
                level.append(node.right)
                level.append(node.left)
                node.next = prev
                prev = node
            level.reverse()
            stack = level
        return root
