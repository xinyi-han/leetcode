from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Recursive
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = list()

        def dfs(node: Node, lst: List[int]):
            if node is None:
                return
            for child in node.children:
                dfs(child, lst)
            lst.append(node.val)

        dfs(root, output)
        return output


# Iterative
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = list()
        stack = list()
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node is None:
                continue
            output.append(node.val)
            for child in node.children:
                stack.append(child)
        output = reversed(output)
        return output
