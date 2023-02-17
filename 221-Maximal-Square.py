from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        edgeLen = 0
        for j in range(n):
            cache[-1][j] = int(matrix[-1][j])
            edgeLen = max(edgeLen, cache[-1][j])
        for i in range(m - 1):
            cache[i][-1] = int(matrix[i][-1])
            edgeLen = max(edgeLen, cache[i][-1])
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if matrix[i][j] == "0":
                    cache[i][j] = 0
                else:
                    cache[i][j] = 1 + min(cache[i][j+1], cache[i+1][j], cache[i+1][j+1])
                    edgeLen = max(edgeLen, cache[i][j])
        return edgeLen**2
