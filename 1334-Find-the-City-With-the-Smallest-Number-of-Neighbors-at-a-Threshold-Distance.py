from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[99999 for _ in range(n)] for _ in range(n)]
        for f, t, w in edges:
            matrix[f][t] = w
            matrix[t][f] = w
        for k in range(n):
            for i in range(n):
                if matrix[i][k] < 99999:
                    for j in range(n):
                        if matrix[k][j] < 99999:
                            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                            matrix[j][i] = matrix[i][j]
        node = n
        minNum = n + 1
        for i in range(n - 1, -1, -1):
            num = sum([0 if w > distanceThreshold or j == i else 1 for j, w in enumerate(matrix[i])])
            if num < minNum:
                minNum = num
                node = i
        return node
