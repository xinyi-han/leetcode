import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [(x, y) for x, y in points]
        pts = set(points)
        prevs = {pt: None for pt in points}
        costs = {pt: float('inf') for pt in points}

        pt = points[0]
        heap = [(0, 0, None, pt)]
        heapq.heapify(heap)
        while len(pts) > 0:
            cost, i, prev, pt = heapq.heappop(heap)
            if pt not in pts:
                continue
            pts.remove(pt)
            prevs[pt] = prev
            costs[pt] = cost
            for j, point in enumerate(pts):
                dis = abs(pt[0] - point[0]) + abs(pt[1] - point[1])
                heapq.heappush(heap, (dis, i+j, pt, point))
        return sum(costs.values())
