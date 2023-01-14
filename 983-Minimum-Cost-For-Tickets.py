from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = [d * costs[0] for d in range(len(days) + 1)]
        for i, day in enumerate(days, 1):
            # cache[i] = min(cache[i], cache[i - 1] + costs[0])
            # Edge case: days = [1,4,6,7,8,20], costs = [7,2,15]
            cache[i] = min(cache[i], cache[i - 1] + min(costs))
            for j in range(1, 31):
                if i - 1 - j < 0:
                    break
                diff = day - days[i - 1 - j]
                if diff >= 30:
                    break
                elif diff < 7:
                    cache[i] = min(cache[i], cache[i - j - 1] + costs[1])
                else:
                    cache[i] = min(cache[i], cache[i - j - 1] + costs[2])
        return cache[-1]
