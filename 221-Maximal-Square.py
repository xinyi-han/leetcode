from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            cache[m - 1][j] = int(matrix[m - 1][j])
        for i in range(m):
            cache[i][n - 1] = int(matrix[i][n - 1])
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if matrix[i][j] == "0":
                    cache[i][j] = 0
                else:
                    cache[i][j] = min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1]) + 1
        return max(list(map(max, cache)))**2
