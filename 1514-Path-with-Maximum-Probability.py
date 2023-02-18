import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # matrix = [[0.0 for _ in range(n)] for _ in range(n)]
        # for k, edge in enumerate(edges):
        #     prob = succProb[k]
        #     i, j = edge
        #     matrix[i][j] = prob
        #     matrix[j][i] = prob
        adjList = {i: [] for i in range(n)}
        for k, edge in enumerate(edges):
            i, j = edge
            prob = succProb[k]
            adjList[i].append((j, prob))
            adjList[j].append((i, prob))
        nodes = set(range(n))
        prevs = {i: None for i in range(n)}
        probs = {i: 0 for i in range(n)}
        heap = [(-1, -1, start)] # prev = -1 for the first node
        heapq.heapify(heap)
        while len(heap) > 0:
            prob, prev, node = heapq.heappop(heap)
            if node not in nodes:
                continue
            nodes.remove(node)
            prevs[node] = prev
            probs[node] = - prob
            if node == end:
                break
            for n, p in adjList[node]:
                if n not in nodes:
                    continue
                heapq.heappush(heap, (prob * p, node, n))
        return probs[end]
