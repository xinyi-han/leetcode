class Solution:
    def mySqrt(self, x: int) -> int:
        return self.binarySearch(0, x, x)

    def binarySearch(self, lo: int, hi: int, target: int) -> int:
        if lo > hi:
            return hi
        mid = (lo + hi) // 2
        sqr = mid**2
        if sqr == target:
            return mid
        elif sqr > target:
            return self.binarySearch(lo, mid - 1, target)
        else:
            return self.binarySearch(mid + 1, hi, target)
