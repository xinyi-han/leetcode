from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = list()

        def dfs(node: Node, lst: List[int]):
            if node is None:
                return
            lst.append(node.val)
            for child in node.children:
                dfs(child, lst)

        dfs(root, output)
        return output


# Iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = list()
        stack = list()
        stack.append(root)
        while len(stack) > 0:
            children = list()
            node = stack.pop()
            if node is None:
                continue
            output.append(node.val)
            for child in node.children:
                children.append(child)
            children.reverse()
            stack.extend(children)
        return output
