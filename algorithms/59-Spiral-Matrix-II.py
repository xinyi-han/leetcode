from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        k = 0
        num = 1
        while k < n // 2:
            for i in range(0 + k, n - 1 - k):
                matrix[0 + k][i] = num
                num += 1
            for j in range(0 + k, n - 1 - k):
                matrix[j][n - 1 - k] = num
                num += 1
            for i in range(1 + k, n - k):
                matrix[n - 1 - k][-i] = num
                num += 1
            for j in range(1 + k, n - k):
                matrix[-j][0 + k] = num
                num += 1
            k += 1
        if n % 2 == 1:
            matrix[k][k] = num
        return matrix
