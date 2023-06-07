# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(1, n)

    def binarySearch(self, lo: int, hi: int) -> int:
        if lo > hi:
            return lo
        mid = (lo + hi) // 2
        if isBadVersion(mid):
            return self.binarySearch(lo, mid - 1)
        else:
            return self.binarySearch(mid + 1, hi)
