from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = list()
        queue = list()
        queue.append(root)
        while len(queue) > 0:
            level = list()
            vals = list()
            for node in queue:
                if node is None:
                    continue
                vals.append(node.val)
                for child in node.children:
                    level.append(child)
            queue = level
            if len(vals) > 0:
                output.append(vals)
        return output
