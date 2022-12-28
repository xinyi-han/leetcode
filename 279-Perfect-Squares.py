class Solution:
    def numSquares(self, n: int) -> int:
        cache = [n for _ in range(n + 1)]
        cache[0] = 0
        sqrs = [j**2 for j in range(1, n + 1) if j**2 <= n]
        for i in range(1, n + 1):
            for j in sqrs:
                if i - j < 0:
                    break
                cache[i] = min(cache[i], 1 + cache[i - j])
        return cache[-1]
