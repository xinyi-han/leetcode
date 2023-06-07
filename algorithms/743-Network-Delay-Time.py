import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i: [] for i in range(1, n + 1)}
        for src, tar, time in times:
            adjList[src].append((tar, time))
        nodes = set(range(1, n + 1))
        prevs = {i: 0 for i in range(1, n + 1)}
        ts = {i: 101 for i in range(1, n + 1)} # maximum time for a signal to travel is 100
        heap = [(0, 0, k)]
        heapq.heapify(heap)
        while len(heap) > 0:
            t, prev, node = heapq.heappop(heap)
            if node not in nodes:
                continue
            nodes.remove(node)
            prevs[node] = prev
            ts[node] = t
            for neighbour, time in adjList[node]:
                if neighbour not in nodes:
                    continue
                heapq.heappush(heap, (t + time, node, neighbour))
        values = list(ts.values())
        total = max(values) # not sum(values)
        return -1 if total == 101 else total
