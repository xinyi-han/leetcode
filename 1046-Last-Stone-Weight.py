import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            fst = heapq.heappop(stones) * -1
            snd = heapq.heappop(stones) * -1
            if snd < fst:
                heapq.heappush(stones, (fst - snd) * (-1))
        return 0 if len(stones) == 0 else stones[0] * -1
