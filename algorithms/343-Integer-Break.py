# JZ14
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        div = n // 3
        mod = n % 3
        if mod == 0:
            return 3**div
        if mod == 1:
            return 2**2 * 3**(div - 1)
        return 2 * 3**div
