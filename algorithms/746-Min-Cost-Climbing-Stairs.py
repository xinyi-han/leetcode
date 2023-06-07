from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [float('inf') for _ in range(len(cost) + 1)]
        cache[0] = 0
        cache[1] = 0
        for i in range(len(cost)):
            cache[i + 1] = min(cache[i + 1], cache[i] + cost[i])
            if i < len(cost) - 1:
                cache[i + 2] = min(cache[i + 2], cache[i] + cost[i])
        return cache[-1]
