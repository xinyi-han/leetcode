class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            div = n // 3
            if 3 * div != n:
                return False
            n = div
        return True
