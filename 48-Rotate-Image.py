from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        k = 0
        while k < n // 2:
            left = [matrix[i][0 + k] for i in range(0 + k, n - 1 - k)]
            bottom = [matrix[n - 1 - k][j] for j in range(0 + k, n - 1 - k)]
            for i in range(0 + k, n - 1 - k):
                matrix[i][0 + k] = bottom[i - k]
            right = [matrix[i][n - 1 - k] for i in range(1 + k, n - k)]
            right.reverse()
            for j in range(0 + k, n - 1 - k):
                matrix[n - 1 - k][j] = right[j - k]
            top = [matrix[0 + k][j] for j in range(1 + k, n - k)]
            for i in range(1 + k, n - k):
                matrix[i][n - 1 - k] = top[i - 1 - k]
            left.reverse()
            for j in range(1 + k, n - k):
                matrix[0 + k][j] = left[j - 1 - k]

            k += 1
