from collections import deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbours = {i: list() for i in range(n)}
        edges = set()
        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
            edges.add((a, b))
        queue = deque([0])
        num = 0
        visit = set()
        while len(queue) > 0:
            node = queue.popleft()
            visit.add(node)
            for neighbour in neighbours[node]:
                if neighbour in visit:
                    continue
                queue.append(neighbour)
                if (neighbour, node) not in edges:
                    num += 1
        return num
