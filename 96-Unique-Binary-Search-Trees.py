class Solution:
    def numTrees(self, n: int) -> int:
        cache = [0 for _ in range(n + 1)]
        cache[0] = 1
        cache[1] = 1
        for i in range(2, n + 1):
            num = 0
            for j in range(1, i + 1):
                num += cache[j - 1] * cache[i - j]
            cache[i] = num
        return cache[-1]
