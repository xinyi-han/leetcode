class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num
        while lo <= hi:
            mid = (lo + hi) // 2
            sqr = mid**2
            if sqr == num:
                return True
            elif sqr > num:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
