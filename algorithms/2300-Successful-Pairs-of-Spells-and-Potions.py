from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def binarySearch(lo: int, hi: int, s: int):
            if lo > hi:
                return lo
            mid = lo + (hi - lo) // 2
            if potions[mid] * s < success:
                return binarySearch(mid + 1, hi, s)
            else:
                return binarySearch(lo, mid - 1, s)

        return list(map(lambda s: len(potions) - binarySearch(0, len(potions) - 1, s), spells))
