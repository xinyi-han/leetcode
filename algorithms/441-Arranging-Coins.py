from typing import Tuple


class Solution:
    def arrangeCoins(self, n: int) -> int:
        i, flag = self.binarySearch(1, n, n)
        return i if flag else i - 1

    def binarySearch(self, lo: int, hi: int, target: int) -> Tuple[int, bool]:
        if lo > hi:
            return lo, False
        mid = (lo + hi) // 2
        sum = (1 + mid) * mid // 2
        if sum == target:
            return mid, True
        elif sum < target:
            return self.binarySearch(mid + 1, hi, target)
        else:
            return self.binarySearch(lo, mid - 1, target)
