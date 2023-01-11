import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        bananas = sum(piles)

        def binarySearch(lo: int, hi: int) -> int:
            if lo > hi:
                return lo
            mid = (lo + hi) // 2
            hours = list(map(lambda p: math.ceil(p / mid), piles))
            if sum(hours) <= h:
                return binarySearch(lo, mid - 1)
            else:
                return binarySearch(mid + 1, hi)

        return binarySearch(1, bananas)
