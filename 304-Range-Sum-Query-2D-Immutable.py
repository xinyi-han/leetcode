from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sum[i][j] = self.sum[i][j - 1] + self.sum[i - 1][j] - self.sum[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.sum[r2][c2] - self.sum[r2][c1 - 1] - self.sum[r1 - 1][c2] + self.sum[r1 - 1][c1 - 1]


# Time Limit Exceeded
# class NumMatrix:
#
#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix
#
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         return sum([sum(self.matrix[r][col1:col2 + 1]) for r in range(row1, row2 + 1)])
