# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None
        nodes = dict()
        stack = list()
        stack.append(node)
        while len(stack) > 0:
            node = stack.pop()
            copy = Node(node.val)
            nodes[node.val] = copy
            for neighbor in node.neighbors:
                if neighbor.val in nodes:
                    copy.neighbors.append(nodes[neighbor.val])
                    nodes[neighbor.val].neighbors.append(copy)
                    continue
                stack = set(stack)
                stack.add(neighbor)
                stack = list(stack)
        return nodes[1]
