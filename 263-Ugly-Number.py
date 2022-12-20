class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        while True:
            div = n // 5
            if n - 5 * div != 0:
                break
            n = div
        while True:
            div = n // 3
            if n - 3 * div != 0:
                break
            n = div
        while True:
            div = n // 2
            if n - 2 * div != 0:
                break
            n = div
        return True if n == 1 else False
