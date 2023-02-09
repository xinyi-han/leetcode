class Solution:
    def numTrees(self, n: int) -> int:
        cache = [0 for _ in range(n + 1)]
        cache[0] = 1
        cache[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                cache[i] += cache[j] * cache[i-1-j]
        return cache[-1]
