from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        columns = set()
        rows = set()
        for r, row in enumerate(matrix):
            if 0 in set(row):
                rows.add(r)
        for c in range(n):
            column = [matrix[r][c] for r in range(m)]
            if 0 in set(column):
                columns.add(c)
        for r in rows:
            for c in range(n):
                matrix[r][c] = 0
        for c in columns:
            for r in range(m):
                matrix[r][c] = 0
