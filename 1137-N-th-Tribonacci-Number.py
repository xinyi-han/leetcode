class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [0 for _ in range(n + 1)]
        if n == 0:
            return cache[-1]
        cache[1] = 1
        if n == 1:
            return cache[-1]
        cache[2] = 1
        if n == 2:
            return cache[-1]
        for i in range(3, n + 1):
            cache[i] = cache[i - 3] + cache[i - 2] + cache[i - 1]
        return cache[-1]
