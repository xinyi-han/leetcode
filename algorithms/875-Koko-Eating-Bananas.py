import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def binarySearch(lo: int, hi: int):
            if lo > hi:
                return lo
            mid = lo + (hi - lo) // 2
            hr = sum(map(lambda pile: int(math.ceil(pile / mid)), piles))
            if hr <= h:
                return binarySearch(lo, mid - 1)
            else:
                return binarySearch(mid + 1, hi)

        return binarySearch(1, max(piles))
