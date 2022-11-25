import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 1
        if x == 0:
            return x
        elif x < 0:
            if abs(n) % 2 == 1:
                sign = -1
            x = abs(x)
        return sign * math.exp(n * math.log(x, math.e))
