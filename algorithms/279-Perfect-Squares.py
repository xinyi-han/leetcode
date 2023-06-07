class Solution:
    def numSquares(self, n: int) -> int:
        maxEdge = int(n**0.5)
        sqrs = list(map(lambda x: x**2, range(1, maxEdge + 1)))
        cache = [n for _ in range(n + 1)]
        cache[0] = 0
        for sqr in sqrs:
            for i in range(1, n + 1):
                if sqr > i:
                    continue
                cache[i] = min(cache[i], 1 + cache[i - sqr])
        return cache[-1]
