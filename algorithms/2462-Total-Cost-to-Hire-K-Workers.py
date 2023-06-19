import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost = 0
        if 2 * candidates >= len(costs):
            heapq.heapify(costs)
            i = 0
            while i < k:
                c = heapq.heappop(costs)
                cost += c
                i += 1
            return cost
        first = costs[:candidates]
        last = costs[-candidates:]
        heapq.heapify(first)
        heapq.heapify(last)
        i = candidates - 1
        j = len(costs) - candidates
        session = 0
        while i + 1 < j:
            if first[0] <= last[0]:
                c = heapq.heappop(first)
                i += 1
                heapq.heappush(first, costs[i])
            else:
                c = heapq.heappop(last)
                j -= 1
                heapq.heappush(last, costs[j])
            cost += c
            session += 1
            if session == k:
                return cost
        while session < k and len(first) > 0 and len(last) > 0:
            if first[0] <= last[0]:
                c = heapq.heappop(first)
            else:
                c = heapq.heappop(last)
            cost += c
            session += 1
        if session == k:
            return cost
        heap = first if len(first) > 0 else last
        while session < k:
            c = heapq.heappop(heap)
            cost += c
            session += 1
        return cost
