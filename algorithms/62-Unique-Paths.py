class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                cache[i][j] = cache[i][j + 1] + cache[i + 1][j]
        return cache[0][0]
